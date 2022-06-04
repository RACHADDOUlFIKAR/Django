from django.contrib import admin
from .models import product
# Register your models here.
@admin.register(product)
class productadmin(admin.ModelAdmin):
    list_display=['id','nom','prix']