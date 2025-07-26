from django.urls import path 
from instructor.views import *

app_name = 'instructor'

urlpatterns = [
    path('instructor-about-learning/' , instructor_about_learning_view , name='instructor_about_learning'),
    path('instructor/' , instructor_view , name='instructor'),
    path('instructor-active-course/' , instructorActiveCourse_view , name='instructorActiveCourse'),
    path('instructor-analytics-course/' , instructorAnalyticsCourse_view , name='instructorAnalyticsCourse'),
    path('instructor-analytics-earning/' , instructorAnalyticsEarning_view , name='instructorAnalyticsEarning'),
    path('instructor-analytics-overview/' , instructorAnalyticsOverview_view , name='instructorAnalyticsOverview'),
]