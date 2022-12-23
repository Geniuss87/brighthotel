from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('blog_single/<int:pk>/', views.BlogSingleView.as_view(), name='blog_single'),
    path('comment/', views.CommentCreateView.as_view(), name='comment'),
    path('post_update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),


]
