from django.test import TestCase

from profiles.models import User
from .models import Blog


class TestBlogViews(TestCase):
    """ Test Blog app views """

    def setUp(self):
        """ Create test information """

        self.blog = Blog.objects.create(
            blog_title='test title',
            blog_content_one='test',
            blog_content_two='test',
            blog_content_three='test',
            author='test',
            image='test '
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

    def test_all_blogs_view(self):
        """ Test that blogs page renders for all users """
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/blogs.html')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        """ Test that blog detail view renders for all users """
        response = self.client.get(f'/blog/{self.blog.id}/')
        self.assertTemplateUsed(response, 'blog/blog_detail.html')
        self.assertEqual(response.status_code, 200)

    def test_add_product_view(self):
        """ Test that only admin can access add_blog page"""

        # Check admin users have access to add blog page
        self.client.force_login(self.admin_user)
        response = self.client.get('/blog/add/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects for logged in users (not admin)
        self.client.force_login(self.user)
        response = self.client.get('/blog/add/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Checked page redirects if not logged in
        response = self.client.get('/blog/add/')
        self.assertEqual(response.status_code, 302)

    def test_edit_product_view(self):
        """ Test that only admin can access edit_blog page"""

        # Check admin users have access to edit product page
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/blog/edit/{self.blog.id}/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects for logged in users (not admin)
        self.client.force_login(self.user)
        response = self.client.get(f'/blog/edit/{self.blog.id}/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Checked page redirects if not logged in
        response = self.client.get(f'/blog/edit/{self.blog.id}/')
        self.assertEqual(response.status_code, 302)
