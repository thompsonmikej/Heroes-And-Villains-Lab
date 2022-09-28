from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/supers/', views.supers_detail),  
    # path('<int:pk>/', views.supers_detail),
]