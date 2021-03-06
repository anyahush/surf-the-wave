from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ Creates OrderForm class """
    class Meta:
        """ Update Class Meta Data """
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county',
                  'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, required attribute
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        labels = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'postcode': 'Postcode',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                self.fields[field].label = labels[field] + ""
                if self.fields[field].required:
                    placeholder = f'{labels[field]} *'
                else:
                    placeholder = labels[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields['country'].label = 'Country'
