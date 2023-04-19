# from django.http import HttpResponse
from django.core.mail import send_mail
from dotenv import load_dotenv
import os
from smtplib import SMTPDataError

# Load environment variables from .env file
# Add variables from .env file to the environment
load_dotenv()


def welcome_email(request):
    """
    Sends a welcome email to the user.
    """
    try:
        # Use Django's send_mail function to send an email to the user.
        send_mail(
            'django-send-mail',
            'Email body of django-send-mail\nWelcome to django-send-mail!',
            'user@some-email.nowhere',
            [os.getenv("MY_VALIDATED_EMAIL")],
        )
        print("Email sent successfully!")
    except Exception as e:
        # The `print` statement and the `return` statement are for illustrative purposes only.  Take a look at their differences. There are better ways to handle exceptions from a user's perspective which are beyond the scope of this example. 
        print(e)
        return e
