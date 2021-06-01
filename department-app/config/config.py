"""Data class for configuration"""
import os
from os import environ
from dataclasses import dataclass


@dataclass
class Config:
    """Set Flask configuration from .env file."""

    # Database Config
    testing = int(environ['testing'])
    db_name = environ['db_name']
    db_host = environ['db_host']
    db_user = environ['db_user']
    db_passwd = environ['db_passwd'] if ('db_passwd' in os.environ) else ''

    # App Config
    sqlalchemy_database_uri = f'mysql+pymysql://{db_user}:{db_passwd}@{db_host}/{db_name}'
    sqlalchemy_track_modifications = False
    secret_key = 'not really secret for a while'
