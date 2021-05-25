"""This script implements Flask app"""

from views import view
from .app import app
from .populate import populate_db

populate_db()

# Views
app.add_url_rule('/', view_func=view.departments)
app.add_url_rule('/departments', view_func=view.departments)
app.add_url_rule('/employees', view_func=view.employees)

if __name__ == '__main__':
    app.run(debug=True)  # pragma: no cover
