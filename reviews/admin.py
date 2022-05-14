from django.contrib import admin
from .models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    """ Allow admin users to manage reviews """

    list_display = (
        'review_title',
        'review_content',
        'author',
        'date_added',
    )
    ordering = ('-date_added',)


admin.site.register(ProductReview, ProductReviewAdmin)