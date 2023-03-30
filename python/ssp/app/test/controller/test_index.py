from app.test.base import BaseTestCase


class TestIndexController(BaseTestCase):

    def test_login(self):
        # when
        with self.client:
            response = self.client.get('/')
        # then
        self.assertEqual(response.status_code, 200)
