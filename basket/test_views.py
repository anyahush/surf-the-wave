from django.test import TestCase
from products.models import Product, Category


class TestBasketViews(TestCase):
    """ Test basket views """
    def setUp(self):
        """ Create test record """
        self.category = Category.objects.create(
            name='testCategory',
            friendly_name='Test Category',
        )

        self.product = Product.objects.create(
            sku='12345',
            name='test product',
            description='test',
            has_sizes='True',
            price='80',
            image_url='test',
            image='test',
            category=self.category,
        )
        self.quantity = 1

        self.basket = {
            f'{self.product.id}': '1',
        }

    def test_basket_view(self):
        """ Test basket view renders """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)

    def test_add_basket_view(self):
        """ Test items can be added to basket """
        basket_data = {
            'product': Product.objects.get(pk=self.product.id),
            'quantity': int(self.quantity),
            'redirect_url': f'/products/{self.product.id}/'
        }
        response = self.client.post(
            f'/basket/add/{self.product.id}', basket_data)
        self.assertEqual(response.status_code, 301)
