import unittest

from rest.app import app


class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.app.testing = True

    # def test_hello_world(self):
    #     home = self.app.get('/')
    #     self.assertIn('Hello World!', str(home.data))
