"""Data class for configuration"""
import os
from os import environ


class Config:
    """Set Flask configuration from .env file."""

    # Database Config
    db_name = environ['db_name']
    db_host = environ['db_host']
    db_user = environ['db_user']
    db_passwd = environ['db_passwd'] if ('db_passwd' in os.environ) else ''

    # App Config
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_passwd}@{db_host}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'not really secret for a while'
