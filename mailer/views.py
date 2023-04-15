from django.http import HttpResponse
from django.core.mail import send_mail
from dotenv import load_dotenv
import os


load_dotenv()


def welcome_email(request):
    send_mail(
        'django-send-mail',
        'Email body of django-send-mail',
        'user@some-email.nowhere',
        [os.getenv("MY_VALID_EMAIL")],
    )
    return HttpResponse("Welcome email sent!")
