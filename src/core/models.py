from django.db import models
from .utils import asset_upload,asset_upload_property
# Create your models here.


class Picture(models.Model):
    thumbnail = models.ImageField(upload_to=asset_upload, null=True, blank=True)
    normal = models.ImageField(upload_to=asset_upload, null=True, blank=True)


class Currency (models.Model):
   code = models.CharField(max_length=5,null=True,help_text='Currency Code example EUR')
   name = models.CharField(max_length=20,null=True,help_text='Currency Name')


class Country (models.Model):
    code = models.CharField(max_length=10, null=True,help_text='Country Code')
    name = models.CharField(max_length=30,null=True, help_text='Country Name')