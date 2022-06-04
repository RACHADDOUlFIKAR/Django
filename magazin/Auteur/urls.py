from django.urls import path
from .views import all_authors,create_author

urlpatterns=[
    path('auteurs',all_authors,name='authors'),
    path('addauthor',create_author,name='new_author'),
]