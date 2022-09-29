from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.super_types_list),  #first argument-- adds subfolders to the URL, second argument with "views" calls the method 
    path('<int:pk>/', views.super_types_detail),
]
