from django.test import TestCase
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from products.models import Category, Product


class TestProfileViews(TestCase):
    """ Test profile views """
    def setUp(self):
        """ Create test record """
        self.user = User.objects.create(
            username='test',
            password='12345',
        )

        self.category = Category.objects.create(
            name='test_category',
            friendly_name='Test Category',
        )

        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            description='test',
            price='100',
            has_sizes='True',
            image='test',
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

        self.lineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
        )

        self.client.force_login(self.user)

    def test_profile_view(self):
        """ Test profile view renders """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_order_history_view(self):
        """ Test correct template for order history """
        response = self.client.get(
            f'/profile/order_history{self.order.order_number}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='checkout/checkout_success.html')
