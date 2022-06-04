from django.contrib import admin
from .models import Auteur

# Register your models here.

admin.site.register(Auteur)

class auteuradmin(admin.ModelAdmin):
    list_display=['id','nom','tel','cin','Email']