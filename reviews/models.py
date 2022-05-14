from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class ProductReview(models.Model):
    """ Creates ProductReview table in database """

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                null=False, related_name='product')
    review_title = models.CharField(max_length=254, null=False, blank=False)
    review_content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date_added = models.DateField(
        auto_now_add=True, null=False, blank=False, editable=False
    )
