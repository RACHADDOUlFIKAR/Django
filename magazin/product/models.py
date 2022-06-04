from django.db import models

# Create your models here.
class product(models.Model):
    id=models.AutoField(primary_key=1)
    nom=models.CharField(max_length=20)
    description=models.CharField(max_length=200,default="Book description")
    prix=models.IntegerField()
    ecrivain=models.CharField(max_length=50,default="Book author")
    image=models.FileField(upload_to="static/images",default=" ")
    def _str_(self):
      return self.nom
