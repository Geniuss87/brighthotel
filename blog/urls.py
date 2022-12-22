from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('blog_single/<int:pk>/', views.BlogSingleView.as_view(), name='blog_single'),
    path('comment/', views.CommentCreateView.as_view(), name='comment'),

]
