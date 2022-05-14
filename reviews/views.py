from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404

from products.models import Product
from reviews.models import ProductReview
from .forms import ReviewForm


def create_review(request, product_id):
    """ A view to allow users to create product reviews """
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm

    if request.method == 'POST':
        previous_review = ProductReview.objects.filter(
            author=request.user
        ).exists()
        if previous_review:
            messages.error(request, f'You have already left a review for this product on {previous_review.date_added}')
        else:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                messages.success(request, 'Successfully added review!')
            else:
                messages.error(request, 'Failed to add review. Please ensure the form is valid')

            return redirect(reverse('product_detail', kwargs={"product_id": product.id}))

    template = 'reviews/create_review.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)