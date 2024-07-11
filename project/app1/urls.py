
from django.contrib import admin
from django.urls import path

from app1 import views
urlpatterns = [
    path('home1/',views.home,name='home')
]
