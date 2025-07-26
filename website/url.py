from django.urls import path 

from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name = 'index'),    
    path('about/', about_view, name = 'about'),    
    path('contact/', contact_view, name = 'contact'),    
    path('cart/', cart_view, name = 'cart'),    
    path('course/', course_view, name = 'course'),    
    path('error/', error_view, name = 'error'),    
    path('event-details/', event_details, name = 'event_details'),    
    path('event/', event_view, name = 'event'),    
    path('faq/', faq_view, name = 'faq'),   
    path('becom-instructor/', becomeInstructorView, name = 'become-instructor'),   
]