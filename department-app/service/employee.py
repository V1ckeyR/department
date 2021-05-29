from flask import make_response
from flask_restful import Resource, abort, reqparse

from models.model import Department, Employee
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

    # @staticmethod
    # def put(department_id):
    #     # form = forms.EmployeeForm()
    #     # departments = Department.query.with_entities(Department.name).all()
    #     # form.department.choices = list(map(lambda i: i[0], departments))
    #
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('name', help="Department name is required", required=True)
    #     args = parser.parse_args()
    #
    #     result = Department.query.filter_by(id=department_id).first()
    #
    #     if not result:
    #         abort(404, message='Department not found')
    #
    #     if args["name"]:
    #         result.name = args["name"].upper()
    #     else:
    #         return 'Name cannot be empty', 400
    #
    #     db.session.commit()
    #
    #     return '', 200
    #
    # @staticmethod
    # def delete(department_id):
    #     result = Department.query.filter_by(id=department_id).first()
    #
    #     if not result:
    #         abort(404, message='Department not found')
    #
    #     db.session.delete(result)
    #     db.session.commit()
    #
    #     return '', 200
