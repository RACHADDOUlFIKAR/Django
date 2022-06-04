from django.urls import path
from .views import *
urlpatterns=[
    path('home',home,name='product'),
    path('books',book,name='book'),
    path('create',create,name='create'),
    path('delete/<int:id>',delete,name='delete'),
    path('update/<int:id>',update,name='update'),
]