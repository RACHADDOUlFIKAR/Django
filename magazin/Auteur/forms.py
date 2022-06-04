from django.forms import ModelForm
from .models import Auteur
class AuteurForm(ModelForm):
    class Meta:
        model =Auteur
        fields ='__all__'