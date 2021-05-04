from django.shortcuts import render, redirect
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# Function to be imported into Blog view.py 
def display_posts():
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    return queryset


def post_detail(request, slug):
    """ Details on Blog Post """
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('detail_post', slug=post.slug)
    else:
        form = CommentForm()

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)
