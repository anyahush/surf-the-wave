from django import forms
from .models import Blog, BlogComment


class BlogForm(forms.ModelForm):
    """ Create BlogForm class """

    class Meta:
        """ Update Class Meta Data """
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'blog_title': 'e.g The wonders of surfing in Scotland',
            'blog_content': 'e.g Surfing in Scotland has been popular...',
            'author': 'Layla Jefferson',
            'image': 'Image Upload',
            'date_created': '23rd August 2022'
        }
        self.fields['blog_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder


class BlogCommentForm(forms.ModelForm):
    """ Creates BlogCommentForm class """

    class Meta:
        """ Update Class Meta Data """
        model = BlogComment
        fields = [
            'blog_comment',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'blog_comment': 'Leave your comment here',
        }
        self.fields['blog_comment'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
