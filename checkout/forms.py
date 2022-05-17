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
        placeholders = {
            'full_name': 'E.g Stephanie Rawlinson',
            'email': 'E.g steph123@gmail.com',
            'phone_number': 'E.g 01463 716 235',
            'street_address1': 'E.g Marybank Farmhouse',
            'street_address2': 'Dolphinton',
            'town_or_city': 'West Linton',
            'postcode': 'EH46 7HG',
            'county': 'South Lanarkshire',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder