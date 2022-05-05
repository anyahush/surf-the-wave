from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ Checkout view """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kn5E0EmnPRxHevNO4eC8rT3olt1lyyOxqS72KJXkE1XR1NFHSejvgOhP60MHVz77fs9MKNeaJiQs9OqGpaHZCT400bakPOtKY',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
