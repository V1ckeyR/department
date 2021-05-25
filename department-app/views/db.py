"""Database initialization function"""

import pymysql
from flask_sqlalchemy import SQLAlchemy
from .config import Config


def database_init(application):
    """Configure app and database, then create DB"""

    name = Config.db_name
    host = Config.db_host
    user = Config.db_user
    password = Config.db_passwd

    application.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    connection = pymysql.connect(host=host, user=user, passwd=password)
    with connection.cursor() as cursor:
        create_db_sql = f"create database if not exists {name};"
        cursor.execute(create_db_sql)
        connection.commit()
    connection.close()

    return SQLAlchemy(application)
