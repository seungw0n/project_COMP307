from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.contrib.auth.forms import UserCreationForm
# # Create your tests here.
#
# class Setup_Class(TestCase):
#     #('username','first_name', 'last_name', 'email', 'password1', 'password2', )
#     def setUp(self):
#         self.user = User.objects.create_user(username="user", email="user@user.com", password="123123")
#
#
#
# class User_Form_Test(TestCase):
#     def test_UserForm_valid(self):
#         form = UserCreationForm(data={'username': "user", 'first_name': "user", 'last_name': "user",
#             'email': "user@user.com", 'password1': "user", 'password2': "user"})
#         self.assertTrue(form.is_valid())
#
#     #Invalid Form data
#     def test_UserForm_invalid(self):
#         form = UserCreationForm(data={'username': "user", 'first_name': "user", 'last_name': "user",
#             'email': "user@user.com", 'password1': "user", 'password2': "user", 'phone': ""})
#         self.assertFalse(form.is_valid())

# class User_Views_Test(SetUp_Class):
    # def test_home_view(self):
    #     # user_login = self.client.login(email="user@user.com", password="a123@123")
    #     # self.assertTrue(user_login)
    #     user_login = self.client.login(user="user", password="123123")
    #     self.assertTrue(user_login)
