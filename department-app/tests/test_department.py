"""Unittest module"""

import os
import unittest

from rest.api import init_api
from rest.app import init_app
from rest.db import db
from rest.populate import populate_db


class TestDepartment(unittest.TestCase):
    """Unittest department class"""

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

    def test_get_departments(self):
        response = self.client.get('/departments')
        self.assertEqual(200, response.status_code)

    def test_successful_get_department(self):
        response = self.client.get('/departments/1')
        self.assertEqual(200, response.status_code)

    def test_fail_get_department(self):
        response = self.client.get('/departments/100')
        self.assertEqual(404, response.status_code)

    def test_successful_add_department(self):
        response = self.client.post('/departments', data=dict(name='test'))
        self.assertEqual(302, response.status_code)

    def test_fail_add_department(self):
        response = self.client.post('/departments', data=dict(name=''))
        self.assertEqual(400, response.status_code)

    def test_successful_edit_department(self):
        response = self.client.get('/departments/edit/1')
        self.assertEqual(200, response.status_code)

        response = self.client.put('/departments/1?name=tester')
        self.assertEqual(200, response.status_code)

        response = self.client.get('/departments/1')
        self.assertIn('tester'.upper(), str(response.data))
        self.assertEqual(200, response.status_code)

    def test_fail_edit_department(self):
        response = self.client.get('/departments/edit/100')
        self.assertEqual(404, response.status_code)

        response = self.client.put('/departments/100?name=tester')
        self.assertEqual(404, response.status_code)

        response = self.client.put('/departments/1?name=')
        self.assertEqual(400, response.status_code)

    def test_successful_delete_department(self):
        response = self.client.delete('/departments/1')
        self.assertEqual(200, response.status_code)

        response = self.client.get('/departments/1')
        self.assertNotIn('George Guerra', str(response.data))

    def test_fail_delete_department(self):
        response = self.client.delete('/departments/100')
        self.assertEqual(404, response.status_code)
