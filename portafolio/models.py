from django.db import models

# Create your models here.
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    date = DateField(default=date. today)
    image = ImageField(upload_to= "portafolio/images")
    url = URLField(blank=True)