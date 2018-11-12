from django.contrib.auth.models import User, Group
from .models import Listing,Currency,Address,PictureListing,Price,Terms
from django.db.models import signals
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

    @receiver(signals.pre_delete, sender=Listing)
    def auto_delete_pictures_on_delete(sender, instance, **kwargs):
        """Deletes file from filesystem
        when corresponding `File` object is deleted.
     """
        if instance._state.adding is False:
            if instance.picture:
                if os.path.isfile(instance.picture.thumbnail.path):
                    os.remove(instance.picture.thumbnail.path)
                    os.remove(instance.picture.normal.path)


class TermsSerializer (serializers.ModelSerializer):
    min = serializers.CharField(write_only=True)
    max = serializers.CharField(write_only=True)

    class Meta:
        model = Listing
        fields = ('min', 'max', 'terms')

    def update(self, instance, validated_data):
        if(instance.terms):
            terms = instance.terms
            terms.minNights = validated_data['min']
            terms.maxNights = validated_data['max']
        else:
            terms = Terms.objects.create(minNights=validated_data['min'], maxNights=validated_data['max'])
            instance.terms = terms

        instance.save()
        return instance


class AddressSerializer (serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('currency', 'basePrice','extraPersonFee')


class ListingSerializer(serializers.ModelSerializer):
    cost = serializers.IntegerField(source='price.basePrice',read_only=True)
    currency = serializers.CharField(source='price.currency.code',read_only=True)
    address = AddressSerializer(required=True, write_only=True, help_text='Address of this listing')
    owner = serializers.IntegerField(write_only=True, required=True,help_text='Owner of this listing')

    class Meta:
        model = Listing
        fields = ('pk','owner','publicName','address','cost','currency','nickname', 'accommodates', 'bedrooms', 'beds','propertyType', 'roomType')
        extra_kwargs = {
            'pk': {'read_only': True},
            'cost': {'read_only': True},
            'currency': {'read_only': True},
            'accommodates': {'read_only': True},
            'bedrooms': {'read_only': True},
            'beds': {'read_only': True},
            'propertyType': {'read_only': True},
            'roomType': {'read_only': True},
            'nickname': {'required': True},
            'publicName': {'read_only': True}
        }

    def create(self, validated_data):
        address_data = validated_data['address']
        user = User.objects.get(pk=validated_data['owner'])
        address = AddressSerializer.create(AddressSerializer(), validated_data=address_data)
        listing = Listing.objects.update_or_create(owner=user,address=address,nickname=validated_data['nickname'])
        return listing



