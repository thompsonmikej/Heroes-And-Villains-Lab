from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.supers_list),  #See views-- this is all objects
    path('<int:pk>/', views.supers_detail), #see views-- this is a particular object
]