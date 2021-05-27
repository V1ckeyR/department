from views import view
from rest import api
from rest.app import app
from rest.populate import populate_db

# populate_db()

if __name__ == '__main__':
    app.run(debug=True)  # pragma: no cover
