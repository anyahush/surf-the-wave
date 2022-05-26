from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """ Test product form functions """
    def test_name_is_required(self):
        """ Test if form submits without name field """
        form = ProductForm({
            'name': '',
            'sku': '12345',
            'description': 'test',
            'has_sizes': 'True',
            'price': '100',
            'image': 'test',
        })
        # Form should be invalid if name not present
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_description_is_required(self):
        """ Test if form submits without email field """
        form = ProductForm({
                'name': 'test',
                'sku': '12345',
                'description': '',
                'has_sizes': 'True',
                'price': '100',
                'image': 'test',
            })
        # Form should be invalid if description not present
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_price_is_required(self):
        """ Test if form submits without price field """
        form = ProductForm({
            'name': 'test',
            'sku': '12345',
            'description': 'test',
            'has_sizes': 'True',
            'price': '',
            'image': 'test',
        })
        # Form should be invalid if email not present
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')
