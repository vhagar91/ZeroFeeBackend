from django.db import models
from .utils import asset_upload,asset_upload_property
# Create your models here.


class Picture(models.Model):
    thumbnail = models.ImageField(upload_to=asset_upload, null=True, blank=True)
    normal = models.ImageField(upload_to=asset_upload, null=True, blank=True)

