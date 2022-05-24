from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """ Creates Contact table in database """

    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True)
    full_name = models.CharField(max_length=254, null=False, blank=False)
    email_from = models.EmailField(max_length=254, null=False, blank=False)
    order_number = models.CharField(max_length=254, null=True, blank=True)
    enquiry = models.TextField(null=False, blank=False)
    enquiry_sent = models.DateField(
        auto_now_add=True, null=False, blank=False, editable=False)
