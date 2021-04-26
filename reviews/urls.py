from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('add_comment/<product_id>', views.add_comment, name="add_comment"),
    path('edit_comment/<product_id>', views.edit_comment, name="edit_comment"),
    path('delete_comment/<product_id>', views.delete_comment, name="delete_comment"),
]
