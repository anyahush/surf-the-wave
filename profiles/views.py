from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm, UserForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display user profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            user_form.save()
            messages.success(request, 'Profile successfully updated')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid')
    else:
        form = UserProfileForm(instance=profile)
        user_form = UserForm(instance=request.user)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'user_form': user_form,
        'profile': profile,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a previous confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


# Used from Music to my Ears, details in README
@login_required
def delete_user(request, user_id):
    """ Delete user account """
    user = request.user.id
    if not request.user.id == user:
        messages.error(request, 'Sorry you cannot do this')
        return redirect(reverse('account_login'))
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.success(request, 'Your account has been successfully deleted')
    return redirect(reverse('home'))