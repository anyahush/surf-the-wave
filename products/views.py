from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from reviews.models import ProductReview
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ A view to display all products, including
    sorting and search queries """
    # Search and sorting query functions used
    # from Boutique Ado, details in README

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # Sorts products by name, category and direction
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        # Searches products based on user query
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display individual product information """

    product = get_object_or_404(Product, pk=product_id)
    reviews = ProductReview.objects.filter(
        product=product).order_by('date_added')
    previous_review = None
    # Check if user has left a product review previous
    if request.user.is_authenticated:
        previous_review = ProductReview.objects.filter(
            author=request.user, product=product,
        ).exists()

    context = {
        'product': product,
        'reviews': reviews,
        'previous_review': previous_review,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Admin users can add a product to the store """
    # If not admin, users are redirected
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do this')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        # If form is valid, form saved and product created
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product.'
                           'Please ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Admin users can edit products in the store """
    # If not admin, users are redirected
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do this')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        # If form valid, form saved and product updated
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} successfully updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to updated product.'
                           'Please ensure the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Admin users can delete products from the store """
    # If not admin user, redirected
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do this')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} successfully deleted')
    return redirect(reverse('products'))
