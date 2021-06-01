"""This module contains app initialization and configuration"""

from flask import Flask
from config import Config


def init_app(uri):
    """App initialization and configuration"""
    new_app = Flask(__name__, template_folder='../templates/', static_folder='../static/')
    new_app.config['SQLALCHEMY_DATABASE_URI'] = uri
    new_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.sqlalchemy_track_modifications
    new_app.config['SECRET_KEY'] = Config.secret_key
    return new_app


app = init_app(Config.sqlalchemy_database_uri)
