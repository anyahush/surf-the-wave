from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """ Test order form functions """
    def test_full_name_is_required(self):
        """ Test if form submits without name field """
        form = OrderForm({
            'full_name': '',
            'phone_number': '1234',
            'email': 'test@test.com',
            'street_address1': 'Test House',
            'street_address2': 'Test Street',
            'town_or_city': 'Test town',
            'county': 'Teston',
            'country': 'Testland',
            'postcode': 'IV3 TES',
        })
        # Form should be invalid if full name not present
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        """ Test if form submits without phoone number field """
        form = OrderForm({
            'full_name': 'test',
            'phone_number': '',
            'email': 'test@test.com',
            'street_address1': 'Test House',
            'street_address2': 'Test Street',
            'town_or_city': 'Test town',
            'county': 'Teston',
            'country': 'Testland',
            'postcode': 'IV3 TES',
        })
        # Form should be invalid if phone number not present
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_email_is_required(self):
        """ Test if form submits without email field """
        form = OrderForm({
            'full_name': 'test',
            'phone_number': '1234',
            'email': '',
            'street_address1': 'Test House',
            'street_address2': 'Test Street',
            'town_or_city': 'Test town',
            'county': 'Teston',
            'country': 'Testland',
            'postcode': 'IV3 TES',
        })
        # Form should be invalid if email not present
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        """ Test if form submits without street_address1 field """
        form = OrderForm({
            'full_name': 'test',
            'phone_number': '1234',
            'email': 'test@test.com',
            'street_address1': '',
            'street_address2': 'Test Street',
            'town_or_city': 'Test town',
            'county': 'Teston',
            'country': 'Testland',
            'postcode': 'IV3 TES',
        })
        # Form should be invalid if image not present
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        """ Test if form submits without town_or_city field """
        form = OrderForm({
            'full_name': 'test',
            'phone_number': '1234',
            'email': 'test@test.com',
            'street_address1': 'Test House',
            'street_address2': 'Test Street',
            'town_or_city': '',
            'county': 'Teston',
            'country': 'Testland',
            'postcode': 'IV3 TES',
        })
        # Form should be invalid if image not present
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_country_is_required(self):
        """ Test if form submits without country field """
        form = OrderForm({
            'full_name': 'test',
            'phone_number': '1234',
            'email': 'test@test.com',
            'street_address1': 'Test House',
            'street_address2': 'Test Street',
            'town_or_city': 'Test town',
            'county': 'Teston',
            'country': '',
            'postcode': 'IV3 TES',
        })
        # Form should be invalid if image not present
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_postcode_is_required(self):
        """ Test if form submits without postcode field """
        form = OrderForm({
            'full_name': 'test',
            'phone_number': '1234',
            'email': 'test@test.com',
            'street_address1': 'Test House',
            'street_address2': 'Test Street',
            'town_or_city': 'Test town',
            'county': 'Teston',
            'country': 'Testland',
            'postcode': '',
        })
        # Form should be invalid if image not present
        self.assertFalse(form.is_valid())
        self.assertIn('postcode', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['postcode'][0], 'This field is required.')

