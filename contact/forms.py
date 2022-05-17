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
        labels = {
            'full_name': 'Full Name',
            'email_from': 'Email',
            'order_number': 'Order Number',
            'enquiry': 'Enquiry'
        }
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = labels[field] + ""
            if self.fields[field].required:
                placeholder = f'{labels[field]} *'
            else:
                placeholder = labels[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder