# myapp/tests.py
from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="tasnim")
        self.assertEqual(user.username, "tasnim")
