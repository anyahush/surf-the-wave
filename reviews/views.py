from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User

from products.models import Product
from reviews.models import ProductReview
from .forms import ReviewForm


def create_review(request, product_id):
    """ A view to allow users to create product reviews """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = User.objects.get(username=request.user.username)
            review.product = product
            review.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', kwargs={"product_id": product.id}))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid')
    else:
        form = ReviewForm()

    template = 'reviews/create_review.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)