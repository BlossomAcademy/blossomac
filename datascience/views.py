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
            send_mail('Subject here', 'Dear Sir/Madam, \n \n Thanks for signing up! We shall be sending you updates from now on. Get ready to blossom! \n Regards, \n Blossom Team', 'info@blossomacademy.co', [sender], fail_silently=True)
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
 