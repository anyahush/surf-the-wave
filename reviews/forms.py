from django import forms
from .models import ProductReview


class ReviewForm(forms.ModelForm):
    """ Create ReviewForm class """

    class Meta:
        """ Update Class Meta Data """
        model = ProductReview
        fields = [
            'review_content',
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, required attribute
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        labels = {
            'review_content': 'Review',
        }

        self.fields['review_content'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = labels[field] + ""
            if self.fields[field].required:
                placeholder = f'{labels[field]} *'
            else:
                placeholder = labels[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder