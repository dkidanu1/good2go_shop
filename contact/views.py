from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    """ A view to return the contact page """

    return render(request, 'contact.html')
