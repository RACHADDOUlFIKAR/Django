from django.db import models

# Create your models here.

class Auteur(models.Model):
    Id=models.AutoField(primary_key=1)
    Nom=models.CharField(max_length=30)
    Tel=models.IntegerField()
    Cin=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    def _str_(self):
       return self.nom
