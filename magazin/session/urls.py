from django.urls import path
from .views import conx,register,logout
urlpatterns=[
    path('',conx,name='connexion'), 
    
    path('register',register,name='registration'), 
    
    path('logout',logout,name='logout'),
]