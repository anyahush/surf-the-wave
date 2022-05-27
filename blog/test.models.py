from django.test import TestCase
from .models import Blog


class TestBlogModels(TestCase):
    """ Test blog app models """

    def setUp(self):
        """ Create test record """
        self.blog = Blog.objects.create(
            blog_title='test title',
            blog_content_one='test',
            blog_content_two='test',
            blog_content_three='test',
            author='test',
            image='test '
        )

    def test_blog_title_string(self):
        """ Test blog title string method """
        self.assertEqual(str(self.blog), 'test title')
