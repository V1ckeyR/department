from rest import api
from rest.app import app
from rest.db import db
from rest.populate import populate_db


@app.before_first_request
def models_init():
    db.create_all()
    # populate_db()


if __name__ == '__main__':
    app.run(debug=True)  # pragma: no cover
