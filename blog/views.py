from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class Post_Detail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# Function to be imported into Blog view.py 
def display_posts():
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    return queryset


def post_detail(request, post_id):
    """ Details on Blog Post """
    post = get_object_or_404(Post, pk=post_id)
    form = form   
    context = {
        'post': post,
        'form': form
    }

    return render(request, 'blog/post_detail.html', context)
