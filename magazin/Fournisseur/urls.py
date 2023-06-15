from django.urls import path
from .views import all_fourn,add_fourn,update_fourn,delete_fourn

urlpatterns=[
    path('fourns',all_fourn,name='fournisseurs'),
    path('addfourn',add_fourn,name='add_fournisseur'),
    path('update_fourn/<int:Id>',update_fourn,name='update_fournisseur'),
    path('delete_fourn/<int:Id>',delete_fourn,name='del_fournisseur'),
]