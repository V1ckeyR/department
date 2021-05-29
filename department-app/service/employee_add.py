from flask import make_response
from flask_restful import Resource

from views.forms import EmployeeForm
from models.model import Department
from views import view


class EmployeeAddResource(Resource):
    @staticmethod
    def get():
        form = EmployeeForm()
        departments = Department.query.with_entities(Department.name).all()
        form.department.choices = list(map(lambda i: i[0], departments))

        response = make_response(view.employee_add(form))
        response.content_type = 'text/html'
        return response
