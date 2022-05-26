from django.test import TestCase
from reviews.forms import ReviewForm


class TestReviewForm(TestCase):
    """ Test review form functions """
    def test_review_content_is_required(self):
        """ Test if form submits without content field """
        form = ReviewForm({
            'review_content': '',
        })
        # Form should be invalid if name not present
        self.assertFalse(form.is_valid())
        self.assertIn('review_content', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['review_content'][0], 'This field is required.')
