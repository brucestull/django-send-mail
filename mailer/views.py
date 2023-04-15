from django.http import HttpResponse
from django.core.mail import send_mail
from dotenv import load_dotenv
import os

load_dotenv()

def index(request):
    return HttpResponse("Goodbuy, World! Send off that message!")


def welcome_email(request):
    send_mail(
        'Welcome to Django',
        'This is a welcome email from Django.',
        'admin@mailer.app',
        [os.getenv("MY_VALID_EMAIL")],
    )
    return HttpResponse("Welcome email sent!")
