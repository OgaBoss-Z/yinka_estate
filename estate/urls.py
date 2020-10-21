from django.contrib import admin
from django.urls import path
from estate import views

urlpatterns = [
   path('', views.home, name='home-page'),
   path('about/', views.about, name='about-page'),
   path('contact/', views.contact, name='contact-page'),
   path('properties/', views.properties, name='properties-page'),
   path('<pk>/<slug>/', views.detail, name='detail-page'),   
]
