from django.contrib import admin
from django.urls import path
from Fardana.views import http_test


urlpatterns = [
    path('', http_test),    

]