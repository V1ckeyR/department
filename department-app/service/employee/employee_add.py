"""This module contains resources for requests with specific id required"""

from flask import make_response
from flask_restful import Resource

from views import view
from views.forms import EmployeeForm
from models.department import Department


class EmployeeAddResource(Resource):
    """Resource class"""
    @staticmethod
    def get():
        """
        This static method exposes GET HTTP method.
        Request processing include select existing record from the database
        :return: response with HTML content
        """
        form = EmployeeForm()
        departments = Department.query.with_entities(Department.name).all()
        form.department.choices = list(map(lambda i: i[0], departments))

        response = make_response(view.employee_add(form))
        response.content_type = 'text/html'
        return response
