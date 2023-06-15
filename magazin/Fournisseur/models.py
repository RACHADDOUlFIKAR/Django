from django.db import models

# Create your models here.

class Fourn(models.Model):
    Id=models.AutoField(primary_key=1)
    Nom=models.CharField(max_length=30)
    Tel=models.IntegerField()
    Adresse=models.CharField(max_length=150)
    Cin=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    def _str_(self):
       return self.Nom
