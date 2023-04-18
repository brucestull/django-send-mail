# from django.http import HttpResponse
from django.core.mail import send_mail
from dotenv import load_dotenv
import os

# Load environment variables from .env file
# Add variables from .env file to the environment
load_dotenv()


def welcome_email(request):
    """
    Sends a welcome email to the user.
    """
    # Use Django's send_mail function to send an email to the user.
    send_mail(
        'django-send-mail',
        'Email body of django-send-mail\nWelcome to django-send-mail!',
        'user@some-email.nowhere', # From email
        [os.getenv("MY_VALIDATED_EMAIL")], # To email(s)
    )
    # The following line will need to be uncommented when this function
    # is changed to a view function since views must return an HttpResponse object.
    # return HttpResponse("Welcome email sent!")
