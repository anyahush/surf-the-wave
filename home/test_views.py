from django.test import TestCase


class TestHomeViews(TestCase):
    """ Tests home page view """
    def test_home_view(self):
        """ Test home page renders """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
