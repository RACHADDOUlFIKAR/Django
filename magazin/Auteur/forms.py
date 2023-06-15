from django.forms import ModelForm
from django import forms
from .models import Auteur
class AuteurForm(ModelForm):
    class Meta:
        model =Auteur
        fields ='__all__'
        widgets = {
            'Nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'Tel':forms.TextInput(attrs={'placeholder':'Telephone'}),
            'Cin':forms.TextInput(attrs={'placeholder':'Cin'}),
            'Email':forms.TextInput(attrs={'placeholder':'Email'})
        }