from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory

# Create your tests here.
from .views import *

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester", email="tester@tester.com", password="testerpassword123")

    def test_get(self):
        request = self.factory.get('/')
        request.user = self.user
        response = home(request)
        self.assertEqual(response.status_code, 200)
