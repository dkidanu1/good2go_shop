from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):


    title = forms.CharField(
        widget=forms.TextInput(
        attrs={"placeholder": "Title",
        "class": "form-control"})
    )
    body = forms.CharField(
        widget=forms.Textarea(
        attrs={"placeholder": "Body",
        "class": "form-control",
        })
    )
    rating = forms.CharField(
        widget=forms.TextInput(
        attrs={"placeholder": "rating",
        "class": "form-control"})
    )

    class Meta:
        model = Comment
        exclude = (
            'user',
            'date_added',
            'product',
            'upvotes',
            'downvotes')

        fields = ('title', 'body', 'rating')

        labels = {
            'rating': 'Rating',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Description',
        }
