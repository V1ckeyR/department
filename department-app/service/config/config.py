"""Data class for configuration"""
from os import environ


class Config:
    """Set Flask configuration from .env file."""

    # Database Config
    db_name = environ['db_name']
    db_host = environ['db_host']
    db_user = environ['db_user']
    db_passwd = environ['db_passwd']

    # App Config
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_passwd}@{db_host}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
