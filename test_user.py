from unittest import TestCase
from app import app


def test_redirection(self):
    with app.test_Users() as User:
        resp = User.get("/redirect")

        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, "http://localhost/")
