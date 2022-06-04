from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    cin=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)