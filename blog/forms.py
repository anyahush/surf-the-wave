from django import forms
from .models import Blog, BlogComment


class BlogForm(forms.ModelForm):
    """ Create BlogForm class """

    class Meta:
        """ Update Class Meta Data """
        model = Blog
        exclude = ('date_created',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, required attribute
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        labels = {
            'blog_title': 'Blog Title',
            'blog_content': 'Blog Content',
            'author': 'Author',
            'image': 'Image Upload',
        }
        self.fields['blog_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = labels[field] + ""
            if self.fields[field].required:
                placeholder = f'{labels[field]} *'
            else:
                placeholder = labels[field]
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
        self.fields['blog_comment'].label = ""
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
