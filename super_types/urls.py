from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.super_types_list)
]
