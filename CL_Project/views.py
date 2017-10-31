from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Basic Home View
def welcome_view(request):
    return render(request, 'home.html')
