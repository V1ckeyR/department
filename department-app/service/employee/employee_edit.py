"""This module contains resources for requests with specific id required"""

from flask import make_response
from flask_restful import Resource

from config.logger import logger
from models import Department
from service.employee.get_employee_by_id import get_employee_by_id
from views import view, forms


class EmployeeEditResource(Resource):
    """Resource class"""
    @staticmethod
    def get(employee_id):
        """
        This static method exposes GET HTTP method.
        Request processing include select existing record from the database
        :return: response with HTML content
        """
        form = forms.EmployeeForm()
        departments = Department.query.with_entities(Department.name).all()
        form.department.choices = list(map(lambda i: i[0], departments))

        employee = get_employee_by_id(employee_id)
        form.department.data = employee.department
        logger.info('Form for editing employee %s', employee)

        response = make_response(view.employee_edit(form, employee))
        response.content_type = 'text/html'
        return response
