from flask import make_response, redirect, flash
from flask_restful import Resource, abort
from sqlalchemy import func

from models import Department, Employee
from rest.db import db
from views.forms import DepartmentForm
from views import view


class DepartmentsResource(Resource):
    @staticmethod
    def get():
        departments = Department.query.join(Employee, isouter=True) \
            .group_by(Department.id) \
            .with_entities(func.round(func.ifnull(func.avg(Employee.salary), 0), 2).label('avg')) \
            .add_columns(Department.id.label('id'), Department.name.label('name')) \
            .all()

        response = make_response(view.departments(departments))
        response.content_type = 'text/html'
        return response

    @staticmethod
    def post():
        form = DepartmentForm()
        if form.validate_on_submit():
            name = form.name.data.upper()

            if Department.query.filter_by(name=name).first():
                abort(409, message='Department already exists')

            db.session.add(Department(name))
            db.session.commit()

            return redirect('/departments')

        flash(f"Validation failed: {form.errors}")
        response = make_response(view.department_add(form))
        response.content_type = 'text/html'
        return response
