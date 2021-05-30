from config import departments_data, employees_data
import models
from rest.db import db


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

    populate_table(db, models.Department, departments_data)
    populate_table(db, models.Employee, employees_data)

