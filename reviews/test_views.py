from django.test import TestCase
from django.contrib.auth.models import User
from .models import ProductReview
from products.models import Product, Category


class TestReviewsViews(TestCase):
    """ Test reviews views """
    def setUp(self):
        """ Create test record """
        self.user = User.objects.create(
            username='terst',
            password='12345',
        )

        self.client.force_login(self.user)

        self.category = Category.objects.create(
            name='test_catergory',
            friendly_name='Test Category',
        )

        self.product = Product.objects.create(
            category=self.category,
            name='testProduct',
            description='testDescription',
            price='100',
            image='test',
        )

        self.review = ProductReview.objects.create(
            product=self.product,
            author=self.user,
            review_content='test',
        )

    def test_create_review_view(self):
        """ Test create review view rendered properly"""
        response = self.client.get(f'/reviews/{self.product.id}/add/')
        self.assertEqual(response.status_code, 200)

    def test_edit_review_view(self):
        """ Test edit review view rendered properly """
        response = self.client.get(f'/reviews/{self.review.id}/edit/')
        self.assertEqual(response.status_code, 200)
