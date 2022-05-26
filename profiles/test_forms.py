from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """ Test user profile form works """
    def test_fields_are_not_required(self):
        """ Test if form submits without fields populated """
        form_data = {
                'default_full_name': '', 
                'default_phone_number': '', 
                'default_street_address1': '',
                'default_street_address2': '',
                'default_town_or_city': '',
                'default_county': '',
                'default_postcode': '',
                'default_country': '',
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)