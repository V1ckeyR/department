from flask import Flask
from flask_migrate import Migrate
from .db import database_init


app = Flask(__name__, template_folder='../templates/', static_folder='../static/')

db = database_init(app)

migrate = Migrate(app, db)
