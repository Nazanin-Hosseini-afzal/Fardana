from django.shortcuts import render

def instructor_view (request) :
    return render (request, 'website/instructor.html')

def instructor_about_learning_view (request) :
    return render (request, 'website/instructor-about-learning.html')

def instructorActiveCourse_view (request) :
    return render (request, 'website/instructor-active-course.html')

def instructorAnalyticsCourse_view (request) :
    return render (request, 'website/instructor-analytics-course.html')

def instructorAnalyticsEarning_view (request) :
    return render (request, 'website/instructor-analytics-earning.html')

def instructorAnalyticsOverview_view (request) :
    return render (request, 'website/instructor-analytics-overview.html')

