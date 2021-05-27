from flask import make_response
from flask_restful import Resource, abort, reqparse
from sqlalchemy import func

from models.model import Department, Employee
from rest.db import db
from views import view

department_parser = reqparse.RequestParser()
department_parser.add_argument('name', help="Department name is required", required=True)


class DepartmentsResource(Resource):
    @staticmethod
    def get():
        departments = Employee.query.join(Department) \
            .group_by(Department.id) \
            .with_entities(func.avg(Employee.salary).label('avg')) \
            .add_columns(Department.id.label('id'), Department.name.label('name')) \
            .all()

        response = make_response(view.departments(departments))
        response.content_type = 'text/html'
        return response

    @staticmethod
    def delete(department_id):
        result = Department.query.filter_by(id=department_id).first()

        if not result:
            abort(404, message='Department not found')

        db.session.delete(result)
        return '', 204


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
            .with_entities(func.avg(Employee.salary).label('avg'))\
            .first()

        response = make_response(view.department(department, employees, round(avg[0], 2)))
        response.content_type = 'text/html'
        return response

    @staticmethod
    def post():
        args = department_parser.parse_args()
        name = args["name"].upper()

        if Department.query.filter_by(name=name).first():
            abort(409, message='Department already exists')

        db.session.add(Department(name))
        db.session.commit()

        result = Department.query.filter_by(name=name).first()
        return result, 201

    @staticmethod
    def put(department_id):
        args = department_parser.parse_args()
        result = Department.query.filter_by(id=department_id).first()

        if not result:
            abort(404, message='Department not found')

        if args["name"]:
            result.name = args["name"].upper()

        db.session.commit()
        return result, 200

    @staticmethod
    def delete(department_id):
        result = Department.query.filter_by(id=department_id).first()

        if not result:
            abort(404, message='Department not found')

        db.session.delete(result)
        return '', 204
