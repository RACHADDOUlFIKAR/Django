from sre_constants import SUCCESS
from tempfile import template
from django.urls import path, reverse_lazy
from parametre import views

from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView

urlpatterns=[
    path('passwordchange/',PasswordChangeView.as_view(template_name='parametre/parametre.html',success_url=reverse_lazy('done')),name='parametre'),
    path('changed/',PasswordChangeDoneView.as_view(template_name='parametre/succes.html'),name='done'),
    path('deletacc/<int:pk>/',views.deleteaccount.as_view(),name='del')
    
    ]