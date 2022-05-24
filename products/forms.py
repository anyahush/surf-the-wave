from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Creates ProductForm class """

    class Meta:
        """ Update Class Meta Data """
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, required attribute
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        labels = {
            'sku': 'SKU',
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Price',
            'image_url': 'Image URL',
        }

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if (
                field != 'category' and
                field != 'has_sizes' and
                field != 'image'
            ):
                self.fields[field].label = labels[field] + ""
                if self.fields[field].required:
                    placeholder = f'{labels[field]} *'
                else:
                    placeholder = labels[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields['category'].label = 'Category'
        self.fields['has_sizes'].label = 'Has Sizes'
        self.fields['image'].label = 'Image Upload'
