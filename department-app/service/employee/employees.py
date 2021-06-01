"""This module contains resources for requests without specific id required"""

from flask import request, make_response, redirect
from flask_restful import Resource, abort
from sqlalchemy import func

from config.logger import logger
from models import Employee, Department
from rest.db import db
from views import view
from views.forms import EmployeeForm


class EmployeesResource(Resource):
    """Resource class"""
    @staticmethod
    def get():
        """
        This static method exposes GET HTTP method.
        Request processing include select existing record from the database
        :return: response with HTML content
        """

        args = request.args
        min_date = Employee.query.with_entities(func.min(Employee.date_of_birth)).first()[0]
        max_date = Employee.query.with_entities(func.max(Employee.date_of_birth)).first()[0]

        start = args["start"] if "start" in args else min_date
        finish = args["finish"] if "finish" in args else max_date

        employees = Employee.query\
            .join(Department)\
            .with_entities(Department.name.label('department'), Employee.id, Employee.name,
                           Employee.surname, Employee.date_of_birth, Employee.salary)\
            .filter(Employee.date_of_birth.between(start, finish))\
            .all()

        logger.info('List of employees: %s', employees)
        response = make_response(view.employees(employees, min_date, max_date, (start, finish)))
        response.content_type = 'text/html'
        return response

    @staticmethod
    def post():
        """
        This static method exposes POST HTTP method.
        Request processing include inserting new record in the database
        :return: response object that redirects to another page
        """

        form = EmployeeForm()
        departments = Department.query.with_entities(Department.name).all()
        form.department.choices = list(map(lambda i: i[0], departments))

        if form.validate_on_submit():
            name = form.name.data.capitalize()
            surname = form.surname.data.capitalize()
            date = form.date.data
            department_name = form.department.data
            department = Department.query.filter_by(name=department_name).with_entities(Department.id).first()[0]
            salary = form.salary.data

            if Employee.query.filter_by(name=name, surname=surname, date_of_birth=date).first():
                logger.warning('Employee not found, aborting')
                abort(409, message='Employee already exists')

            db.session.add(Employee((name, surname, department, date, salary)))
            db.session.commit()

            new_id = Employee.query.filter_by(name=name, surname=surname, date_of_birth=date)\
                .with_entities(Employee.id).first()[0]

            logger.info('Employee successfully created, redirecting...')
            return redirect(f'/employees/{new_id}')

        logger.warning('Employee add form not valid or submitted')
        return '', 400
