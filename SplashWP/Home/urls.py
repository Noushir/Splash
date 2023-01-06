from django.urls import path , include
from . import views
urlpatterns = [
   
    path('', views.index,name='home'),
    path('login/',views.login,name='login'),
    path('sign-up/',views.sign_up,name='signup'),    
    path('dashboard/', views.dash,name='dash'),
    path('contact/', views.contact,name='contact'),
]