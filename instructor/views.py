from django.shortcuts import render

def instructor_view (request) :
    return render (request, 'website/instructor.html')

def instructor_about_learning_view (request) :
    return render (request, 'website/instructor-about-learning.html')
