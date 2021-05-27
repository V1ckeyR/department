from flask_restful import Api

from rest.app import app
from service import department

api = Api(app)
api.add_resource(department.DepartmentsResource, '/', '/departments')
api.add_resource(department.DepartmentResource, '/departments/<int:department_id>')
api.add_resource(department.DepartmentAddResource, '/departments/add')
api.add_resource(department.DepartmentEditResource, '/departments/edit/<int:department_id>')
