'''
This is the url module for app foo
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]
