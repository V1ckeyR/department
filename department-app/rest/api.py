"""This module contains api initialization and resources adding"""
import logging

from flask_restful import Api

from rest.app import app
import service


def init_api(application):
    """API initialization and configuration"""
    logging.info('API initialization and configuration')
    new_api = Api(application)

    new_api.add_resource(service.DepartmentsResource, '/', '/departments')
    new_api.add_resource(service.DepartmentResource, '/departments/<int:department_id>')
    new_api.add_resource(service.DepartmentAddResource, '/departments/add')
    new_api.add_resource(service.DepartmentEditResource, '/departments/edit/<int:department_id>')

    new_api.add_resource(service.EmployeesResource, '/employees')
    new_api.add_resource(service.EmployeeResource, '/employees/<int:employee_id>')
    new_api.add_resource(service.EmployeeAddResource, '/employees/add')
    new_api.add_resource(service.EmployeeEditResource, '/employees/edit/<int:employee_id>')

    return new_api


api = init_api(app)
