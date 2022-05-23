from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from profiles.models import UserProfile
from .forms import ContactForm


def contact(request):
    """ A view to render the contact page """

    if request.method == 'POST':
        # If post method successful get information from form
        form_data = {
            'full_name': request.POST['full_name'],
            'email_from': request.POST['email_from'],
            'order_number': request.POST['order_number'],
            'enquiry': request.POST['enquiry'],
        }
        contact_form = ContactForm(form_data)

        if contact_form.is_valid():
            user_enquiry = contact_form.save(commit=False)
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user)
                user_enquiry.user = user
            user_enquiry.save()
            send_confirmation_email(user_enquiry)
            messages.success(request, 'Your enquiry has been sent. Check your emails for a confirmation')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'There was an error with your enquiry. Please ensure the form is valid')
            return redirect(reverse('contact'))
    else:
        if request.user.is_authenticated:
            # If user is logged in try and populate information
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'full_name': profile.default_full_name,
                    'email_from': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
        template = 'contact/contact.html'
        context = {
            'contact_form': contact_form,
        }

        return render(request, template, context)


def send_confirmation_email(user_enquiry):
    """ Send a confirmation email following successful enquiry """
    cust_email = user_enquiry.email_from
    subject = 'Thank you for contacting Surf the Wave'
    body = render_to_string(
        'contact/confirmation_emails/confirmation_email_body.txt',
        {'contact': user_enquiry})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )