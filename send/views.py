from django.shortcuts import render 
from django.conf import settings 
from django.core.mail import send_mail 
from django.http import HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response  


def index(request): 
    if request.method == 'POST':
        date=request.POST['date']
        time=request.POST['time'] 
        email=request.POST['email']
        message=request.POST['message'] 
        email_body = f"Date: {date}\nTime: {time}\n\nMessage: {message}" 
        send_mail( 
            'Remind me later', #title 
            email_body, 
            settings.EMAIL_HOST_USER, 
            [email], 
        fail_silently=False) 
    return render(request, 'index.html')


































































# Create your views here.
