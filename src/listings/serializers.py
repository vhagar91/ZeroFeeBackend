from django.contrib.auth.models import User, Group
from .models import *
from src.core.models import Picture
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.utils.six import text_type
from django.dispatch import receiver
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
import os


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = PictureListing
        fields = ('id' , 'thumbnail', 'normal')

    @receiver(models.signals.pre_delete, sender=Listing)
    def auto_delete_pictures_on_delete(sender, instance, **kwargs):
        """Deletes file from filesystem
        when corresponding `File` object is deleted.
     """
        if instance._state.adding is False:
            if instance:
                if os.path.isfile(instance.picture.thumbnail.path):
                    os.remove(instance.picture.thumbnail.path)
                    os.remove(instance.picture.normal.path)


class TermsSerializer (serializers.ModelSerializer):

    class Meta:
        model = Terms
        fields = ('minNights', 'maxNights')


class AddressSerializer (serializers.ModelSerializer):
    class Meta:
        model = Address


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('currency', 'basePrice','extraPersonFee')


class ListingSerializer(serializers.ModelSerializer):
    price = PriceSerializer()

    class Meta:
        model = Listing
        fields = ('price', 'term','nickname', 'accommodates', 'bedrooms', 'beds','checkInTime', 'checkOutTime', 'propertyType', 'roomType')

