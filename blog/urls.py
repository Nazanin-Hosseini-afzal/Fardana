from django.urls import path 
from blog.views import *

app_name = 'blog'

urlspatterns = [
    path (' ' blog , blog_view , name='index'),
    path('single' , blog_single, name='single')
]