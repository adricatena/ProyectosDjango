from django.urls import path
from cucinaDiTatiApp import views

urlpatterns = [
    path('', views.home, name=''),
    path('home/', views.home, name='home'),
]
