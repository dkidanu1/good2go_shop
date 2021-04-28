from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def aboutus(request):
    """ A view to return the aboutus page """

    return render(request, 'home/aboutus.html')
