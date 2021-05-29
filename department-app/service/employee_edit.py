from flask import make_response
from flask_restful import Resource, abort

from models.model import Employee, Department
from views import view, forms


class EmployeeEditResource(Resource):
    @staticmethod
    def get(employee_id):
        form = forms.EmployeeForm()
        departments = Department.query.with_entities(Department.name).all()
        form.department.choices = list(map(lambda i: i[0], departments))

        employee = Employee.query \
            .filter_by(id=employee_id) \
            .join(Department) \
            .with_entities(Department.name.label('department'), Employee.id, Employee.name,
                           Employee.surname, Employee.date_of_birth, Employee.salary)\
            .first()

        if not employee:
            abort(404, message='Employee not found')

        form.department.data = employee.department

        response = make_response(view.employee_edit(form, employee))
        response.content_type = 'text/html'
        return response
