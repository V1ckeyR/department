"""This script run application on a local development server"""

from config.logger import logger
from rest.api import app
from rest.db import db
from rest.populate import populate_db


@app.before_first_request
def models_init():  # pragma: no cover
    """Initialization of models and population db with test data if we need so"""
    db.create_all()
    is_database_empty = False
    logger.info('Before first request database is empty: %s', is_database_empty)
    if is_database_empty:
        populate_db()


if __name__ == '__main__':
    app.run(debug=True)  # pragma: no cover
