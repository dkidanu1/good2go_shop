from django.shortcuts import render
from  blog.views import display_posts


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def aboutus(request):
    """ A view to return the aboutus page """

    posts = display_posts()
    context = {
        'post_list': posts
    }

    return render(request, 'home/aboutus.html', context)
