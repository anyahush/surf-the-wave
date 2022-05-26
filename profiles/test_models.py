from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class TestProductModels(TestCase):
    """ Test profile app models """

    def setUp(self):
        """ Create test record """

        self.user = User.objects.create(
            username='test',
            password='12345',
        )
        self.userprofile = UserProfile.objects.get(user=self.user)

    def test_profile_string(self):
        """ Test Profile string method """
        self.assertEqual(str(self.userprofile), 'test')
