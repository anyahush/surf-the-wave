from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Outlines what fields we want admin to see """
    list_display = (
        'full_name',
        'email_from',
        'order_number',
        'enquiry',
        'enquiry_sent',
    )
    ordering = ('-enquiry_sent',)


admin.site.register(Contact, ContactAdmin)
