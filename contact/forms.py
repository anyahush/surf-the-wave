from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Create ContactForm class """

    class Meta:
        """ Update Class Meta Data """
        model = Contact
        exclude = ('user', 'message_sent')

    def __init__(self, *args, **kwargs):
        """ Add placeholders and required attribute,
        set autofocus on first field """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'e.g Hannah Matheson',
            'email': 'e.g hannahmatheson1@yahoo.com',
            'order_number': 'FD405F66C443497B804C9BF0C28AB653',
            'enquiry': 'Hello, Could do you know if you are getting more of...'
        }
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder