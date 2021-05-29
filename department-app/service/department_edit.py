from flask import make_response
from flask_restful import Resource, abort

from models.model import Department
from views import view


class DepartmentEditResource(Resource):
    @staticmethod
    def get(department_id):
        department = Department.query.filter_by(id=department_id).first()

        if not department:
            abort(404, message='Department not found')

        response = make_response(view.department_edit(department))
        response.content_type = 'text/html'
        return response
