from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """ A view that renders the bag contents """
    template = 'basket/basket.html'
    context = {
        'on_basket': True,
    }

    return render(request, template, context)


def add_to_basket(request, item_id):
    """ Add a quantity of specified product to shopping basket """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    # If the product has a size
    if size:
        # If the product exists in the basket
        if item_id in list(basket.keys()):
            # If the product is in the basket with the same size
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 f'Updated size {size.upper()}'
                                 f'{product.name} quantity'
                                 f'to {basket[item_id]["items_by_size"]}')
            # If product is in basket but not the same size
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 f'Added size {size.upper()}'
                                 f'{product.name} to your basket')
        # If product is not in the basket
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             f'Added size {size.upper()}'
                             f'{product.name} to your basket')
    # If the product has no size
    else:
        # If the product exists in the basket
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request,
                             f'Updated {product.name} quantity'
                             f'to {basket[item_id]}')
        # If the product doesn't exist in the basket
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust quantity of specified product to shopping basket """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})
    print(basket)

    # If product has a size
    if size:
        # If the quantity greated than 0, updates the quantity
        # to show new quantity
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             f'Updated size {size.upper()}'
                             f'{product.name} quantity')
        # Otherwise removes product from basket
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request,
                             f'Removed size {size.upper()}'
                             f'{product.name} from your basket')
    # If product has no size
    else:
        # If the quantity greated than 0, updates the quantity
        # to show new quantity
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity')
        # Otherwise removes product from basket
        else:
            basket.pop(item_id)
            messages.success(request,
                             f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove product to shopping basket """

    product = get_object_or_404(Product, pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        # If product has a size
        if size:
            # Removes selected product
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request,
                             f'Removed size {size.upper()}'
                             f'{product.name} from your basket')
        # If product has not size
        else:
            # Removes selected product
            basket.pop(item_id)
            messages.success(request,
                             f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
