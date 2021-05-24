from models import model
from .config import departments_data, employees_data


def populate_table(database, table, data):
    """
    Populate table with test data

    :param database: SQLAlchemy object
    :param table: db.Model
    :param data: test data array
    """

    for row in data:
        database.session.add(table(row))
        database.session.commit()


def populate_db():
    """Populate tables with test data"""

    populate_table(model.db, model.Department, departments_data)
    populate_table(model.db, model.Employee, employees_data)
