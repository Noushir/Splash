from django.urls import path , include
from . import views
urlpatterns = [
   
    path('', views.index),
    path('login/',views.login),
    path('sign-up/',views.sign_up),    
    path('dashboard/', views.dash),
]