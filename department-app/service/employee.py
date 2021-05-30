from flask import make_response
from flask_restful import Resource, abort, reqparse

from models import Employee, Department
from rest.db import db
from views import view


class EmployeeResource(Resource):
    @staticmethod
    def get(employee_id):
        employee = Employee.query \
            .filter_by(id=employee_id) \
            .join(Department)\
            .with_entities(Department.name.label('department'), Employee.id, Employee.name,
                           Employee.surname, Employee.date_of_birth, Employee.salary)\
            .first()

        if not employee:
            abort(404, message='Employee not found')

        response = make_response(view.employee(employee))
        response.content_type = 'text/html'
        return response

    @staticmethod
    def put(employee_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', help="Employee name is required")
        parser.add_argument('surname', help="Employee surname is required")
        parser.add_argument('date', help="Employee date is required")
        parser.add_argument('department', help="Employee department is required")
        parser.add_argument('salary', help="Employee salary is required")
        args = parser.parse_args()

        result = Employee.query.filter_by(id=employee_id).first()

        if not result:
            abort(404, message='Employee not found')

        if args["name"]:
            result.name = args["name"].capitalize()

        if args["surname"]:
            result.surname = args["surname"].capitalize()

        if args["date"]:
            result.date_of_birth = args["date"]

        if args["department"]:
            department_name = args["department"]
            result.department = Department.query.filter_by(name=department_name).with_entities(Department.id).first()[0]

        if args["salary"]:
            result.salary = args["salary"]

        db.session.commit()
        return '', 200

    @staticmethod
    def delete(employee_id):
        result = Employee.query.filter_by(id=employee_id).first()

        if not result:
            abort(404, message='Employee not found')

        db.session.delete(result)
        db.session.commit()

        return '', 200
