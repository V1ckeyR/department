"""This module contains resources for requests with specific id required"""

from flask import make_response
from flask_restful import Resource, abort, reqparse

from config.logger import logger
from models import Employee, Department
from rest.db import db
from service.employee.get_employee_by_id import get_employee_by_id
from views import view


class EmployeeResource(Resource):
    """Resource class"""
    @staticmethod
    def get(employee_id):
        """
        This static method exposes GET HTTP method.
        Request processing include select existing record from the database
        :param employee_id: The variable is used for database query
        :return: response with HTML content
        """

        response = make_response(view.employee(get_employee_by_id(employee_id)))
        response.content_type = 'text/html'
        return response

    @staticmethod
    def put(employee_id):
        """
        This static method exposes PUT HTTP method.
        Request processing include updating existing record in database
        :param employee_id: The variable is used for database query
        :return: status code
        """

        parser = reqparse.RequestParser()
        parser.add_argument('name', help="Employee name is required")
        parser.add_argument('surname', help="Employee surname is required")
        parser.add_argument('date', help="Employee date is required")
        parser.add_argument('department', help="Employee department is required")
        parser.add_argument('salary', help="Employee salary is required")
        args = parser.parse_args()

        result = Employee.query.filter_by(id=employee_id).first()

        if not result:
            logger.warning('Employee not found, aborting')
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

        logger.info('Updating employee: %s', result)
        db.session.commit()
        return '', 200

    @staticmethod
    def delete(employee_id):
        """
        This static method exposes DELETE HTTP method.
        Request processing include deleting existing record in database
        :param employee_id:
        :return: status code
        """

        result = Employee.query.filter_by(id=employee_id).first()

        if not result:
            logger.warning('Employee not found, aborting')
            abort(404, message='Employee not found')

        logger.info('Deleting employee %s with id %s', result, employee_id)
        db.session.delete(result)
        db.session.commit()
        return '', 200
