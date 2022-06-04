from django.urls import path
from .views import session,conx,register,logout
urlpatterns=[
    path('session',conx,name='connexion'),  
    path('register',register,name='registration'), 
    path('logout',logout,name='logout'),
]