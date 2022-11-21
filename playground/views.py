from django.core.mail import send_mail , mail_admins , BadHeaderError , EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_cusmtomer

def say_hello(request):
    #try:
        #send_mail('subject','message','info@moshbuy.com',['bob@moshbuy.com'])
        #mail_admins('subject','message',html_message='message')
        #{message = EmailMessage('subject','message','from@moshbuy.com',['jhon@moshbuy.com'])
        #message.attach_file('playground/static/images/aks.jpeg')
        #message.send()  }
        #message = BaseEmailMessage(template_name='emails/hello.html',
        #context={'name' : 'Mosh'})
        #message.send(['jhon@moshbuy.com'])
    #except BadHeaderError:
    #    pass
    return render(request, 'hello.html', {'name': 'Mosh'})
