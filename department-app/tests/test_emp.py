"""Unittest module"""

import os
import unittest

from rest.api import init_api
from rest.app import init_app
from rest.db import db
from rest.populate import populate_db


class TestEmployee(unittest.TestCase):
    """Unittest employee class"""

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app = init_app('sqlite:///' + os.path.join(basedir, 'test.db'))
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.app_context().push()

        db.init_app(app)
        db.create_all()
        populate_db()

        self.app = init_api(app).app
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_employees(self):
        response = self.client.get('/employees')
        self.assertEqual(200, response.status_code)

    def test_successful_get_employee(self):
        response = self.client.get('/employees/1')
        self.assertEqual(200, response.status_code)

    def test_fail_get_employee(self):
        response = self.client.get('/employees/100')
        self.assertEqual(404, response.status_code)

    def test_successful_add_employee(self):
        response = self.client.post('/employees', data=dict(
            name='test',
            surname='tester',
            date='2010-09-02',
            department='SALES',
            salary='1000'
        ))

        self.assertEqual(302, response.status_code)

    def test_fail_add_employee(self):
        response = self.client.post('/employees', data=dict(name=''))
        self.assertEqual(400, response.status_code)

    def test_successful_edit_employee(self):
        response = self.client.get('/employees/edit/1')
        self.assertEqual(200, response.status_code)

        response = self.client.put('/employees/1?name=tester')
        self.assertEqual(200, response.status_code)

        response = self.client.get('/employees/1')
        self.assertIn('tester'.capitalize(), str(response.data))
        self.assertEqual(200, response.status_code)

    def test_fail_edit_employee(self):
        response = self.client.get('/employees/edit/100')
        self.assertEqual(404, response.status_code)

        response = self.client.put('/employees/100?name=tester')
        self.assertEqual(404, response.status_code)

    def test_successful_delete_employee(self):
        response = self.client.delete('/employees/1')
        self.assertEqual(200, response.status_code)

        response = self.client.get('/employees/1')
        self.assertNotIn('George Guerra', str(response.data))

    def test_fail_delete_employee(self):
        response = self.client.delete('/employees/100')
        self.assertEqual(404, response.status_code)
