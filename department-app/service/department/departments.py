"""This module contains resources for requests without specific id required"""

from flask import make_response, redirect
from flask_restful import Resource, abort
from sqlalchemy import func

from config.logger import logger
from models import Department, Employee
from rest.db import db
from views import view
from views.forms import DepartmentForm


class DepartmentsResource(Resource):
    """Resource class"""
    @staticmethod
    def get():
        """
        This static method exposes GET HTTP method.
        Request processing include select existing record from the database
        :return: response with HTML content
        """

        departments = Department.query.join(Employee, isouter=True) \
            .group_by(Department.id) \
            .with_entities(func.round(func.ifnull(func.avg(Employee.salary), 0), 2).label('avg')) \
            .add_columns(Department.id.label('id'), Department.name.label('name')) \
            .all()

        logger.info('List of departments: %s', departments)
        response = make_response(view.departments(departments))
        response.content_type = 'text/html'
        return response

    @staticmethod
    def post():
        """
        This static method exposes POST HTTP method.
        Request processing include inserting new record in the database
        :return: response object that redirects to another page
        """

        form = DepartmentForm()
        if form.validate_on_submit():
            name = form.name.data.upper()

            if Department.query.filter_by(name=name).first():
                logger.warning('Department not found, aborting')
                abort(409, message='Department already exists')

            db.session.add(Department(name))
            db.session.commit()
            logger.info('Department successfully created, redirecting...')
            return redirect('/departments')

        logger.warning('Department add form not valid or submitted')
        return '', 400
