from flask import make_response
from flask_restful import Resource, abort, reqparse
from sqlalchemy import func

from models.model import Department, Employee
from rest.db import db
from views import view


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
        parser = reqparse.RequestParser()
        parser.add_argument('name', help="Department name is required", required=True)
        args = parser.parse_args()

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
