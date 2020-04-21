from django.test import TestCase
from django.contrib.auth.models import User
from .forms import *
from django.core import mail
# Create your tests here.

class Setup_Class(TestCase):
    #('username','first_name', 'last_name', 'email', 'password1', 'password2', )
    def setUp(self):
        self.user = User.objects.create_user(username="user", email="user@user.com", password="123123")



class Email_Form_Test(TestCase):
    def test_EmailForm_valid(self):
        form = ContactForm(data={'from_email': "user@user.com", 'subject': "user", 'message': "user"})
        self.assertTrue(form.is_valid())

    #Invalid Form data
    def test_EmailForm_invalid(self):
        form = ContactForm(data={'from_email': "user", 'subject': "user", 'message': "user", 'phone': ""})
        self.assertFalse(form.is_valid())


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('subject', 'message', 'from@example.com', ['to@example.com'], fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'subject')
