"""This module contains resources for requests with specific id required"""

from flask import make_response
from flask_restful import Resource, abort, reqparse
from sqlalchemy import func

from models import Department, Employee
from rest.db import db
from views import view
from config.logger import logger


class DepartmentResource(Resource):
    """Resource class"""
    @staticmethod
    def get(department_id):
        """
        This static method exposes GET HTTP method.
        Request processing include select existing record from the database
        :param department_id: The variable is used for database query
        :return: response with HTML content
        """

        department = Department.query.filter_by(id=department_id).first()

        if not department:
            logger.warning('Department not found, aborting')
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
        """
        This static method exposes PUT HTTP method.
        Request processing include updating existing record in database
        :param department_id: The variable is used for database query
        :return: status code
        """

        parser = reqparse.RequestParser()
        parser.add_argument('name', help="Department name is required", required=True)
        args = parser.parse_args()

        result = Department.query.filter_by(id=department_id).first()

        if not result:
            logger.warning('Department not found, aborting')
            abort(404, message='Department not found')

        if args["name"]:
            result.name = args["name"].upper()
        else:
            return 'Name cannot be empty', 400

        logger.info('Updating department: %s', result)
        db.session.commit()
        return '', 200

    @staticmethod
    def delete(department_id):
        """
        This static method exposes DELETE HTTP method.
        Request processing include deleting existing record in database
        :param department_id:
        :return: status code
        """

        result = Department.query.filter_by(id=department_id).first()

        if not result:
            logger.warning('Department not found, aborting')
            abort(404, message='Department not found')

        logger.info('Deleting department %s with id %s', result, department_id)
        db.session.delete(result)
        db.session.commit()
        return '', 200
