from django.urls import path 

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('blog-stories/' , blog_view , name='blog-stories'),
    path('blog-details/' , blog_single, name='blog-details'),
]