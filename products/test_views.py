from django.test import TestCase

from profiles.models import User
from .models import Product, Category


class TestProductsViews(TestCase):
    """ Test Products app views """

    def setUp(self):
        """ Create test information """

        self.category = Category.objects.create(
            name='test_category',
            friendly_name='Test Category',
        )

        self.product = Product.objects.create(
            category=self.category,
            name='testProduct',
            description='testDescription',
            price='100',
            image='test',
        )

        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='admin12345',
            email='admin@test.com',
        )

        self.user = User.objects.create_user(
            username='user',
            password='user12345',
            email='user@test.com',
        )

    def test_all_products_view(self):
        """ Test that products page renders for all users """
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        """ Test that product detail view renders for all users """
        response = self.client.get(f'/products/{self.product.id}/')
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.status_code, 200)
    
    def test_add_product_view(self):
        """ Test that only admin can access add_product page"""

        # Check admin users have access to add product page
        self.client.force_login(self.admin_user)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects for logged in users (not admin)
        self.client.force_login(self.user)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Checked page redirects if not logged in
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)

    def test_edit_product_view(self):
        """ Test that only admin can access edit_product page"""

        # Check admin users have access to edit product page
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/products/edit/{self.product.id}/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects for logged in users (not admin)
        self.client.force_login(self.user)
        response = self.client.get(f'/products/edit/{self.product.id}/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Checked page redirects if not logged in
        response = self.client.get(f'/products/edit/{self.product.id}/')
        self.assertEqual(response.status_code, 302)
