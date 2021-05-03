from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Avg

from products.models import Product
from .models import Comment
from .forms import CommentForm
from profiles.models import UserProfile


def reviews(request):
    return render(request, 'reviews/reviews.html')


def product_detail(request, slug):
    template_name = 'reviews/reviews.html'
    post = get_object_or_404(Product, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'product': Product,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
                                     
                                       
def add_comment(request, product_id):
    """
    Allows a user to add a review and redirect them back to the
    item view
    """
    #user = UserProfile.objects.get(user=request.user)
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    review_form = CommentForm()
   
    review_details = {
        'title': request.POST['title'],
        'body': request.POST['body'],
        'rating': request.POST['rating'],
    }
    review_form = CommentForm(review_details)

    # If the form is valid, add user and product and save
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = user
        review.product = product
        review.save()

        reviews = Comment.objects.filter(product=product)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        product.avg_rating = int(avg_rating)
        product.save()

        messages.success(request, 'Thank you for your review')
    else:
        messages.error(request, 'Something went wrong. '
                                'Make sure the form is valid.')

    return redirect('/products/{}'.format(product_id))


def edit_comment(request, review_id):
    """
    Saves the review form that is edited by a user
    """
    review = get_object_or_404(Comment, pk=review_id)
    review_form = CommentForm(request.POST, instance=review)
    product = Product.objects.get(name=review.product)
    if review_form.is_valid():
        review.save()

        reviews = Comment.objects.filter(product=product)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        product.avg_rating = int(avg_rating)
        product.save()

        # Success message if added
        messages.success(request, 'Thank You! Your review was edited')
    else:
        # Error message if form was invalid
        messages.error(request, 'Something went wrong. '
                                'Make sure the form is valid.')

    #return redirect(reverse('product_detail', args=(review.product.id,)))
    return redirect('/products/{}'.format(product.id)) 


def delete_comment(request, review_id):
    """
    Deletes user's review
    """
    review = get_object_or_404(Comment, pk=review_id)
    product = Product.objects.get(name=review.product)

    try:
        review.delete()

        comments = Comment.objects.filter(product=product)
        avg_rating = Comment.aggregate(Avg('rating'))['rating__avg']
        if avg_rating:
            product.avg_rating = int(avg_rating)
        else:
            product.avg_rating = 0

        product.save()
        messages.success(request, 'Your review was deleted')

    # If deletion failed, return an error message
    except Exception as e:
        messages.error(request, "We couldn't delete your review because "
                                f" error:{e} occured. Try again later.")

    #return redirect(reverse('product_detail', args=(review.product.id,)))
    return redirect('/products/{}'.format(product.id))

