from django.test import TestCase
from django.contrib.messages import get_messages
from django.core import mail


class TestContactViews(TestCase):
    """ Test contact views """
    def test_contact_view(self):
        """ Test contact page renders """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_form(self):
        """ Test contact form is sent """
        full_name = 'test_name'
        email_from = 'test@test.com'
        order_number = '12345'
        enquiry = 'test'

        data = {
            'full_name': full_name,
            'email_from': email_from,
            'order_number': order_number,
            'enquiry': enquiry,
        }

        response = self.client.post('/contact/', data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Your enquiry has been sent.Check your emails for a confirmation')


class TestEmails(TestCase):
    """ Test emails sent """
    def test_send_email(self):
        """ Test if email sent when form submitted """
        mail.send_mail('Subject', 'This is the enquiry',
                       'from@test.com', ['to@test,com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject')
