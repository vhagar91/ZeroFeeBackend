from django.db import models
from .utils import asset_upload
# Create your models here.


class Picture(models.Model):
    thumbnail = models.ImageField(upload_to=asset_upload, null=True, blank=True)
    normal = models.ImageField(upload_to=asset_upload, null=True, blank=True)


class Address(models.Model):
    full = models.CharField(max_length=250, null=True, help_text='Full address')
    lng = models.FloatField(help_text='Geo Longitude',null=True)
    lat = models.FloatField(help_text='Geo Latitude',null=True)
    street = models.CharField(max_length=200,null=True,help_text='Street')
    city = models.CharField(max_length=200,null=True,help_text='City')
    country = models.CharField(max_length=200,null=True,help_text='Country')
