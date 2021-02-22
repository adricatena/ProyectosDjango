from django.urls import path
from cucinaDiTatiApp import views

urlpatterns = [
    path('', views.home, name=''),
    path('home/', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('tienda/', views.tienda, name='tienda'),
    path('contacto/', views.contacto, name='contacto'),
    path('blog/', views.blog, name='blog'),
]
