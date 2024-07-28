from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('post', views.blogPost, name='blog-post'),
]
