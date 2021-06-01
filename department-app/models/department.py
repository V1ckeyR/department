"""This module contains ORM model that represents Department entity"""

from rest.db import db


class Department(db.Model):
    """ORM model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employees = db.relationship('Employee', lazy=True, cascade="all, delete")

    def __init__(self, name):
        self.name = name

    def __repr__(self):  # pragma: no cover
        return 'Department id: {}, name: {}'.format(self.id, self.name)
