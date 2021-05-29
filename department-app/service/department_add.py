from flask import make_response
from flask_restful import Resource

from views.forms import DepartmentForm
from views import view


class DepartmentAddResource(Resource):
    @staticmethod
    def get():
        response = make_response(view.department_add(DepartmentForm()))
        response.content_type = 'text/html'
        return response
