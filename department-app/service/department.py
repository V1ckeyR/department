from flask import make_response, redirect, flash
from flask_restful import Resource, abort, reqparse
from sqlalchemy import func

from models.model import Department, Employee
from rest.db import db
from rest.forms import DepartmentForm
from views import view

department_parser = reqparse.RequestParser()
department_parser.add_argument('name', help="Department name is required", required=True)


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

        flash("Validation failed")
        response = make_response(view.department_add(form))
        response.content_type = 'text/html'
        return response


class DepartmentResource(Resource):
    @staticmethod
    def get(department_id):
        department = Department.query.filter_by(id=department_id).first()

        if not department:
            abort(404, message='Department not found')

        employees = Employee.query.join(Department)\
            .filter(Department.id == department_id).all()

        avg = Employee.query.join(Department)\
            .filter(Department.id == department_id)\
            .with_entities(func.round(func.ifnull(func.avg(Employee.salary), 0), 2).label('avg'))\
            .first()

        response = make_response(view.department(department, employees, avg[0]))
        response.content_type = 'text/html'
        return response

    @staticmethod
    def put(department_id):
        args = department_parser.parse_args()
        result = Department.query.filter_by(id=department_id).first()

        if not result:
            abort(404, message='Department not found')

        if args["name"]:
            result.name = args["name"].upper()
        else:
            return 'Name cannot be empty', 400

        db.session.commit()

        return '', 200

    @staticmethod
    def delete(department_id):
        result = Department.query.filter_by(id=department_id).first()

        if not result:
            abort(404, message='Department not found')

        db.session.delete(result)
        db.session.commit()

        return '', 200


class DepartmentAddResource(Resource):
    @staticmethod
    def get():
        response = make_response(view.department_add(DepartmentForm()))
        response.content_type = 'text/html'
        return response


class DepartmentEditResource(Resource):
    @staticmethod
    def get(department_id):
        department = Department.query.filter_by(id=department_id).first()

        if not department:
            abort(404, message='Department not found')

        response = make_response(view.department_edit(department))
        response.content_type = 'text/html'
        return response
