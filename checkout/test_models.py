from django.test import TestCase
from products.models import Category, Product
from .models import Order, OrderLineItem


class TestCheckoutModels(TestCase):
    """ Test checkout app models """

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

        self.product1 = Product.objects.create(
            name='Test Product1',
            description='test product',
            has_sizes='True',
            price='110',
        )

        self.order = Order.objects.create(
            full_name='Test Testing',
            email='test@test.com',
            phone_number='12345',
            street_address1='Test House',
            postcode='IV3 TES',
            town_or_city='test',
            country='Test',
        )

    def test_order_number_created(self):
        """ Test Order number generated """
        self.assertTrue(self.order.order_number)

    def test_order_string(self):
        """ Test order string method """
        self.assertEqual(str(self.order), str(self.order.order_number))

