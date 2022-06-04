from django.forms import ModelForm
from .models import product
class productForm(ModelForm):
    class Meta:
        model =product
        fields ='__all__'