from django.test import TestCase
from rest_framework.status import HTTP_201_CREATED
from rest_framework.test import APIClient

from wedding.core.tests import factory


class AuthorizationTestCase(TestCase):
    def test_obtain_token_success(self):
        u = factory.UserFactory.create(username='user1')
        u.set_password('password')
        u.save()

        data = {
            'username': u.username,
            'password': u.password
        }
        client = APIClient()
        response = client.post('/core/api-token-auth/', data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
