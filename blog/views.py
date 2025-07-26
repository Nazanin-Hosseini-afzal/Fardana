from django.shortcuts import render

def blog_view (request) :
    return render (request, 'blog-stories.html')

def blog_single (request) :
    return render (request, 'blog-details.html')