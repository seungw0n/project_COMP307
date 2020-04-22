from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from .models import Product
from django.utils import timezone

# Create your tests here.
from .views import *

class SimpleTest(TestCase):
    def setUp(self):
        # Using RequestFactory
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester", email="tester@tester.com", password="testerpassword123")

    def test_get(self):
        request = self.factory.get('/')
        request.user = self.user
        # I can use request.user = AnonymousUser instead of above code.
        response = home(request)
        self.assertEqual(response.status_code, 200)


class PostTest(TestCase):
    def setUp(self):
        # owner = models.ForeignKey(User, on_delete=models.CASCADE, default ='1')
        # title = models.TextField()
        # description = models.TextField(max_length=10000)
        # image_url = models.FileField(upload_to=get_upload_path)
        # inventoryCount = models.IntegerField(default=0)
        # created = models.DateTimeField(auto_now_add=True)
        # price = models.FloatField()
        # category = models.TextField()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester", email="tester@tester.com", password="testerpassword123")
        self.test_product = Product(owner=self.user, title="testTitle",
            description="test_description", image_url="/", inventoryCount="100",
            created="timezone.now()", price="100", category="Outer")
        self.test_product.save()

    def test_Get_product_page(self):
        request = self.factory.get('product/<int:self.test_product.product_id>')
        request.user = self.user
        response = home(request)
        self.assertTrue(response.status_code, 200)
