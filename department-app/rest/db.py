"""Database initialization function"""

import pymysql
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from rest.app import app


def database_init(application):
    """Configure app and database, then create DB"""

    name = Config.db_name
    host = Config.db_host
    user = Config.db_user
    password = Config.db_passwd

    connection = pymysql.connect(host=host, user=user, passwd=password)
    with connection.cursor() as cursor:
        cursor.execute(f"create database if not exists {name};")
        connection.commit()
    connection.close()

    return SQLAlchemy(application)


db = database_init(app)
migrate = Migrate(app, db)
