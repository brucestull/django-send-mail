# Import the `send_mail` function so we can use it to send an email
from django.core.mail import send_mail
# Import the `os` module so we can use it to access environment variables
import os

def welcome_email(request):
    """
    Use the `send_mail` function to send an email to a user's mailgun-validated
    email address.

    The arguments are as follows:
    * `subject` - The subject of the email
    * `message` - The body of the email
    * `from_email` - The email address of the sender
    * `recipient_list` - A list of email addresses of the recipients
        * This example uses only one email address, which is retrieved
        via the environment variable `MY_VALIDATED_EMAIL`.
    """

    # Call Django's `send_mail` function to send an email
    send_mail(
        # `subject`
        'Welcome to Django - In Subject',
        # `message`
        'This is a welcome email from Django - In Body',
        # `from_email`
        'admin@fakeemail.app',
        # `recipient_list`
        [os.getenv('MY_VALIDATED_EMAIL')],
    )
