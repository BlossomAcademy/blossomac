from django.shortcuts import render

from django.core.mail import EmailMessage

from django.http import HttpResponse
from django.core.mail import send_mail

import os
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import ContactForm
from .models import Feedback
#from sendgrid.helpers.mail import *
#import sendgrid
informationB = Feedback.objects.all


form = ContactForm()


def home(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass


            #subject = form.cleaned_data['subject']
            #message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            """sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('YOUR_SENDGRID_API_KEY'))
            from_email = Email("info@blossomacademy.co")
            subject = "Hello World from the SendGrid Python Library!"
            to_email = Email(sender)
            content = Content("text/plain", "Hello, Email!")
            mail = Mail(from_email, subject, to_email, content)
            #response = sg.client.mail.send.post(request_body=mail.get())"""
            """sg = sendgrid.SendGridClient(os.getenv('YOUR_SENDGRID_API_KEY', 'default_value'))
            message = sendgrid.Mail()
            message.add_to(sender)
            message.set_from('app104690940@heroku.com')
            message.set_subject('Confirmation of Subscription')
            message.set_html('Dear Sir/Madam, \n \n Thanks for signing up! We shall be sending you updates from now on. Get ready to blossom! \n Regards, \n Blossom Team')
            sg.send(message)"""
            email = EmailMessage('Confirmation of Subscription', "Welcome! \n \n We believe there are massive pools of incredibly talented youth across Africa; it is imperative to connect them to the global economy. What do you believe today? \n Thank you for signing up to receive email updates from Blossom Academy. Since you have decided to join us on our exciting journey, we promise to provide you with the best experience possible. \n Keep on believing, \n
The Blossom Academy Team", to=[sender])
            email.send()
            """send_mail('Subject here', 'Here is the message.', 'info@blossomacademy.co', [sender], fail_silently=True)"""
            feedback = Feedback(sender=sender)
            feedback.save()

            return HttpResponseRedirect(reverse('index')) # Redirect after POST
    else:
        form = ContactForm() # An unbound form
    return render(request, 'basic.html', {'form': form})


    #return render(request, 'basic.html', {'informationB': informationB })
    #return HttpResponse(' <p> home view </p>')

def join_blossom(request):
    
    return render(request, 'join.html', {'form': form})

def become_partner(request):
    return render(request, 'partner.html', {'form': form})

def about_us(request):
    return render(request, 'about.html', {'form': form})

def privacy_policy(request):
    return render(request, 'privacy_policy.html', {'form': form})

def terms_services(request):
    return render(request, 'terms.html', {'form': form})

def faqs(request):
    return render(request, 'faqs.html', {'form': form})

# Create your views here.
 