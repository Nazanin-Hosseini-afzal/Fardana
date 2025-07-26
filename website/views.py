from django.http import HttpResponse
from django.shortcuts import render




def index_view (request):
    return render(request , 'website/index.html')


def about_view (request):
    return render(request, 'website/about.html')


def contact_view (request):
    return render(request, 'website/contact.html')

def becomeInstructorView(request):
    return render(request, 'website/become-instructor.html')

def cart_view (request) :
    return render(request, 'website/cart.html')

def course_view (request) :
    return render(request, 'website/course.html')

def error_view (request) :
    return render(request, 'website/error.html')

def event_details (request) :
    return render(request, 'website/event-details.html')

def event_view (request) :
    return render(request, 'website/event.html')

def faq_view (request) :
    return render(request, 'website/faq.html')