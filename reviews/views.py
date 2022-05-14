from django.shortcuts import render

from django.shortcuts import render, redirect, reverse, get_object_or_404

from products.models import Product




def create_review(request, product_id):
    """ A view to allow users to create product reviews """

    product = get_object_or_404(Product, pk=product_id)

    template = 'reviews/create_review.html'
    context = {
        'product': product,
    }

    return render(request, template, context)