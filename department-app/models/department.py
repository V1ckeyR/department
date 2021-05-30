from rest.db import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employees = db.relationship('Employee', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Department id: {}, name: {}'.format(self.id, self.name)
