from app.test.base import BaseTestCase
from unittest.mock import patch
import json


class TestLoginController(BaseTestCase):
    def setUp(self):
        self.dupa = "test"

    @patch('app.main.service.AuthenticateService', autospec=True)
    def test_shouldReturnAccessToken(self, mock_user):
        # given
        credentials = {
            "username": "test",
            "password": "test"
        }
        # when
        with self.client:
            response = self.client.post('/auth/login', data=json.dumps(credentials), content_type='application/json')
        # then
        self.assert401(response)
        self.assertEqual(self.dupa, "test")
