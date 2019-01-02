from django.db import models
from .utils import asset_upload,asset_upload_property
from PIL import Image
import os
from django.core.files.base import ContentFile
from io import BytesIO
# Thumbnail size tuple defined in an app-specific settings module - e.g. (400, 400)
from zeroAppBackend.settings import THUMB_SIZE
# Create your models here.


class Picture(models.Model):
    thumbnail = models.ImageField(upload_to=asset_upload, null=True, blank=True)
    normal = models.ImageField(upload_to=asset_upload, null=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(Picture, self).save(*args, **kwargs)

    def make_thumbnail(self):

        image = Image.open(self.normal)
        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.normal.name)
        thumb_extension = thumb_extension.lower()
        filename = thumb_name.split('/')[-1].split('.')[0]
        thumb_filename = filename + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True


class Currency (models.Model):
   code = models.CharField(max_length=5,null=True,help_text='Currency Code example EUR')
   name = models.CharField(max_length=20,null=True,help_text='Currency Name')


class Country (models.Model):
    code = models.CharField(max_length=10, null=True,help_text='Country Code')
    name = models.CharField(max_length=30,null=True, help_text='Country Name')