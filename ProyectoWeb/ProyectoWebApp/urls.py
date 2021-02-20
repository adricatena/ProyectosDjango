from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.home),
    path('servicios/', views.servicios),
    path('tienda/', views.tienda),
    path('blog/', views.blog),
    path('contacto/', views.contacto),
]
