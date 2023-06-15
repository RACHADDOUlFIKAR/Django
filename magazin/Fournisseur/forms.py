from django.forms import ModelForm
from django import forms
from .models import Fourn
class FournForm(ModelForm):
    class Meta:
        model =Fourn
        fields ='__all__'
        widgets = {
            'Nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'Tel':forms.TextInput(attrs={'placeholder':'Telephone'}),
            'Adresse':forms.TextInput(attrs={'placeholder':'adresse'}),
            'Cin':forms.TextInput(attrs={'placeholder':'Cin'}),
            'Email':forms.TextInput(attrs={'placeholder':'Email'})
        }