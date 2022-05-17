from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Creates UserProfileForm class """
    class Meta:
        """ Update Class Meta Data """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, required attribute
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        labels = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postcode',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                self.fields[field].label = labels[field] + ""
                if self.fields[field].required:
                    placeholder = f'{labels[field]} *'
                else:
                    placeholder = labels[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

