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
            'image': 'Image upload',
        }

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'category' and field != 'men_sizes' and field != 'ladies_sizes' and field != 'kids_sizes' and field != 'shoe_sizes' and field != 'kids_shoe_sizes':
                self.fields[field].label = labels[field] + ""
                if self.fields[field].required:
                    placeholder = f'{labels[field]} *'
                else:
                    placeholder = labels[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields['category'].label = 'Category'
        self.fields['men_sizes'].label = 'Mens Sizes'
        self.fields['ladies_sizes'].label = 'Ladies Sizes'
        self.fields['shoe_sizes'].label = 'Shoe Sizes'
        self.fields['kids_sizes'].label = 'Kids Sizes'
        self.fields['kids_shoe_sizes'].label = 'Kids Shoe Sizes'