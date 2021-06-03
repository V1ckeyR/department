"""This module contains resources for requests with specific id required"""

from flask import make_response
from flask_restful import Resource, abort

from config.logger import logger
from models import Department
from views import view


class DepartmentEditResource(Resource):
    """Resource class"""
    @staticmethod
    def get(department_id):
        """
        This static method exposes GET HTTP method.
        Request processing include select existing record from the database
        :return: response with HTML content
        """
        department = Department.query.filter_by(id=department_id).first()

        if not department:
            logger.warning('Department not found, aborting')
            abort(404, message='Department not found')

        logger.info('Form for editing department %s', department)
        response = make_response(view.department_edit(department))
        response.content_type = 'text/html'
        return response
