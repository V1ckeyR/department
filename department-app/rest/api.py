from flask_restful import Api

from rest.app import app
import service

api = Api(app)

api.add_resource(service.DepartmentsResource, '/', '/departments')
api.add_resource(service.DepartmentResource, '/departments/<int:department_id>')
api.add_resource(service.DepartmentAddResource, '/departments/add')
api.add_resource(service.DepartmentEditResource, '/departments/edit/<int:department_id>')

api.add_resource(service.EmployeesResource, '/employees')
api.add_resource(service.EmployeeResource, '/employees/<int:employee_id>')
api.add_resource(service.EmployeeAddResource, '/employees/add')
api.add_resource(service.EmployeeEditResource, '/employees/edit/<int:employee_id>')
