from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from products.models import Product
from reviews.models import ProductReview
from .forms import ReviewForm


@login_required
def create_review(request, product_id):
    """ A view to allow users to create product reviews """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # Filters reviews based on session user
        previous_review = ProductReview.objects.filter(
            author=request.user
        ).exists()
        if previous_review:
            # If previous review error message displayed
            messages.error(request, 'You have already left a comment for this product')
        else:
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


@login_required
def edit_product_review(request, review_id):
    """ A view to all users to edit product reviews"""

    review = get_object_or_404(ProductReview, id=review_id)
    product = review.product

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review successfully updated')
            return redirect(reverse('product_detail', kwargs={"product_id": product.id}))
        else:
            messages.error(request, 'Failed to updated review. Please ensure the form is valid')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing a review for {product.name}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'product': product,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_product_review(request, review_id):
    """ View to allow users to delete product reviews """

    review = get_object_or_404(ProductReview, id=review_id)
    product = review.product

    if review:
        review.delete()
        messages.success(request, f'Review for {product} was successfully deleted')
    else:
        messages.error(request, f'Unable to delete review for {product}')

    return redirect(reverse('product_detail', kwargs={"product_id": product.id}))