from django.core.mail import send_mail
import random
from django.conf import Settings
from .models import User


def send_otp(email):
    subject = 'your account verification email'
    otp = random.randit(1000/9999)
    message = 'Your otp is {otp}'
    email_from= Settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj=User.objects.get(email=email)
    user_obj.otp=otp
    user_obj.save()
    