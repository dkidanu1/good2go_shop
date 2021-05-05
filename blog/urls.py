from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.Post_Detail.as_view(), name='post_detail'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
]
