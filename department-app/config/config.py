"""Data class for configuration"""

from os import getenv
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Config:
    """Set Flask configuration from .env file."""

    load_dotenv()

    # Database Config
    testing = int(getenv('testing'))
    db_name = getenv('db_name')
    db_host = getenv('db_host')
    db_user = getenv('db_user')
    db_passwd = getenv('db_passwd') if getenv('db_passwd') else ''

    # App Config
    sqlalchemy_database_uri = f'mysql+pymysql://{db_user}:{db_passwd}@{db_host}/{db_name}'
    sqlalchemy_track_modifications = False
    secret_key = 'not really secret for a while'
