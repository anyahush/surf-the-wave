from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """ Test contact form functions """
    def test_full_name_is_required(self):
        """ Test if form submits without name field """
        form = ContactForm({
            'full_name': '',
            'email_from': 'test@test.com',
            'enquiry': 'test',
        })
        # Form should be invalid if name not present
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        """ Test if form submits without email field """
        form = ContactForm({
            'full_name': 'test',
            'email_from': '',
            'enquiry': 'test',
        })
        # Form should be invalid if email not present
        self.assertFalse(form.is_valid())
        self.assertIn('email_from', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['email_from'][0], 'This field is required.')

    def test_enquiry_is_required(self):
        """ Test if form submits without enquiry field """
        form = ContactForm({
            'full_name': 'test',
            'email_from': 'test@test.com',
            'enquiry': '',
        })
        # Form should be invalid if email not present
        self.assertFalse(form.is_valid())
        self.assertIn('enquiry', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['enquiry'][0], 'This field is required.')
