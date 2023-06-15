from django.forms import ModelForm
from django import forms
from .models import product
class productForm(forms.ModelForm):
    class Meta:
        model =product
       
        fields ='__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'description':forms.TextInput(attrs={'placeholder':'Description'}),
            'prix':forms.TextInput(attrs={'placeholder':'Prix'}),
            'ecrivain':forms.TextInput(attrs={'placeholder':'Ecrivain'})   
        }