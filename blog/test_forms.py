from django.test import TestCase
from .forms import BlogForm, BlogCommentForm


class TestBlogForm(TestCase):
    """ Test blog form functions """
    def test_blog_title_is_required(self):
        """ Test if form submits without title field """
        form = BlogForm({
            'blog_title': '',
            'blog_content_one': 'test',
            'author': 'test',
            'image': 'test',
        })
        # Form should be invalid if title not present
        self.assertFalse(form.is_valid())
        self.assertIn('blog_title', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['blog_title'][0], 'This field is required.')

    def test_blog_content_is_required(self):
        """ Test if form submits without email field """
        form = BlogForm({
            'blog_title': 'test',
            'blog_content_one': '',
            'author': 'test',
            'image': 'test',
        })
        # Form should be invalid if blog_content_one not present
        self.assertFalse(form.is_valid())
        self.assertIn('blog_content_one', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['blog_content_one'][0], 'This field is required.')

    def test_author_is_required(self):
        """ Test if form submits without price field """
        form = BlogForm({
            'blog_title': 'test',
            'blog_content_one': 'test',
            'author': '',
            'image': 'test',
        })
        # Form should be invalid if author not present
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['author'][0], 'This field is required.')

    def test_image_is_required(self):
        """ Test if form submits without price field """
        form = BlogForm({
            'blog_title': 'test',
            'blog_content_one': 'test',
            'author': 'test',
            'image': '',
        })
        # Form should be invalid if image not present
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['image'][0], 'This field is required.')


class TestBlogCommentForm(TestCase):
    """ Tests blog comment form functions """
    def test_blog_comment_is_required(self):
        """ Test if form submits without price field """
        form = BlogCommentForm({
            'blog_comment': '',
        })
        # Form should be invalid if image not present
        self.assertFalse(form.is_valid())
        self.assertIn('blog_comment', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['blog_comment'][0], 'This field is required.')
