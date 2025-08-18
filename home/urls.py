from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('contact/',views.contact-us,name="contact-us"),
    
]