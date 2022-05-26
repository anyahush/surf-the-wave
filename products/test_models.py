from django.test import TestCase
from .models import Category, Product


class TestProductModels(TestCase):
    """ Test product app models """

    def setUp(self):
        """ Create test record """
        self.category = Category.objects.create(
            name='test',
            friendly_name='Test'
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='test',
            has_sizes='True',
            price='100',
        )

    def test_category_string(self):
        """ Test Category string method """
        self.assertEqual(str(self.category), 'test')
    
    def test_category_friendly(self):
        """ Test Category friendly method """
        self.assertEqual(str(self.category.friendly_name), 'Test')
    
    def test_product_string(self):
        """ Test Product string method """
        self.assertEqual(str(self.product), 'Test Product')
