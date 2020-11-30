from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['earthtomemphis@gmail.com']
        )
        email.fail_silently=False
        email.send()
    
    return render(request, 'email_sent.html')