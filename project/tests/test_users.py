import json

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    def test_users(self):
        """确保ping的服务正常."""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])
