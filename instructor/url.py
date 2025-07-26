from django.urls import path 
from instructor.views import *

app_name = 'instructor'

urlspatterns = [
    path('instructor-about-learning/' , instructor_about_learning_view , name='instructor_about_learning'),
    path('instructor/' , instructor_view , name='instructor'),
]