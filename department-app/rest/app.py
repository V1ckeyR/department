"""This script implements basic Flask implementation"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Returns home page"""
    return 'Hello World!'


if __name__ == '__main__':
    app.run()  # pragma: no cover
