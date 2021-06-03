"""Function to remove code duplication"""

from flask_restful import abort

from config.logger import logger
from models import Employee, Department


def get_employee_by_id(employee_id):
    """
    Get employee by id
    :param employee_id: The variable is used for database query
    :return: query result
    """
    employee = Employee.query \
        .filter_by(id=employee_id) \
        .join(Department) \
        .with_entities(Department.name.label('department'), Employee.id, Employee.name,
                       Employee.surname, Employee.date_of_birth, Employee.salary) \
        .first()

    if not employee:
        logger.warning('Employee not found, aborting')
        abort(404, message='Employee not found')

    return employee
