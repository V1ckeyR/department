"""This module contains resources for requests with specific id required"""

from flask import make_response
from flask_restful import Resource

from views.forms import DepartmentForm
from views import view


class DepartmentAddResource(Resource):
    """Resource class"""
    @staticmethod
    def get():
        """
        This static method exposes GET HTTP method.
        Request processing include select existing record from the database
        :return: response with HTML content
        """

        response = make_response(view.department_add(DepartmentForm()))
        response.content_type = 'text/html'
        return response
