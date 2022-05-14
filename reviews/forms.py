from django import forms
from .models import ProductReview


class ReviewForm(forms.ModelForm):
    """ Create ReviewForm class """

    class Meta:
        """ Update Class Meta Data """
        model = ProductReview
        fields = [
            'review_title',
            'review_content',
        ]
        labels = {
            'review_title': 'Title',
            'review_content': 'Review',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_title': 'e.g Amazing quality!',
            'review_content': 'e.g First wetsuit and it is fabulous...',
            'author': 'Joe Rennie',
            'date_created': '23rd August 2022'
        }
        self.fields['review_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder