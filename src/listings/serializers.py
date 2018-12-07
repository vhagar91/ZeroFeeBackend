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
    thumb = serializers.ImageField(source='thumbnail')
    src = serializers.ImageField(source='normal')

    class Meta:
        model = PictureListing
        fields = ('id','thumb', 'src', 'is_portrait')

    @receiver(signals.pre_delete, sender=PictureListing)
    def auto_delete_pictures_on_delete(sender, instance, **kwargs):
        """Deletes file from filesystem
        when corresponding `File` object is deleted.
     """
        if instance._state.adding is False:
            if instance.picture:
                if os.path.isfile(instance.picture.thumbnail.path):
                    os.remove(instance.picture.thumbnail.path)
                    os.remove(instance.picture.normal.path)



class ListingTermsSerializer (serializers.ModelSerializer):
    minNights = serializers.CharField(write_only=True, help_text='minimun nights stay')
    maxNights = serializers.CharField(write_only=True, help_text='maximun nights stay')
    min = serializers.CharField(read_only=True,source='terms.minNights')
    max = serializers.CharField(read_only=True,source='terms.maxNights')

    class Meta:
        model = Listing
        fields = ('min', 'max', 'minNights','maxNights')

    def update(self, instance, validated_data):

        if instance.terms:
            terms = instance.terms
            terms.minNights = validated_data['minNights']
            terms.maxNights = validated_data['maxNights']
            terms.save()
        else:
            terms = Terms.objects.create(minNights=validated_data['minNights'], maxNights=validated_data['maxNights'])
            instance.terms = terms

        instance.save()
        return instance


class AddressSerializer (serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class CurrencySerializer (serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'


class PriceSerializer (serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ('currency', 'basePrice', 'extraPersonFee', 'breakfastFee')

    def update(self, instance, validated_data):
        currency_id = validated_data['currency_id']
        if instance.currency:
            if instance.currency.id == currency_id:
               validated_data['currency'] = instance.currency
               super(PriceSerializer, self).update(instance,validated_data)
            else:
                cur = Currency.objects.get(pk=currency_id)
                validated_data['currency'] = cur
                super(PriceSerializer, self).update(instance,validated_data)


class ListingPriceSerializer(serializers.ModelSerializer):
    currency = serializers.IntegerField(source='price.currency_id', help_text='Currency', required=False)
    basePrice = serializers.FloatField(source='price.basePrice', help_text='Base Price', required=False)
    extraPersonFee = serializers.FloatField(source='price.extraPersonFee', help_text='Fee for a extra person', required=False)
    breakfastFee = serializers.FloatField(source='price.breakfastFee', help_text='breakfast price', required=False)

    class Meta:
        model = Listing
        fields = ('currency', 'basePrice','extraPersonFee','breakfastFee')

    def update(self, instance, validated_data):
        price_data = validated_data['price']
        if instance.price:
            PriceSerializer.update(PriceSerializer(), instance.price, price_data)
        else:
            curr = Currency.objects.get(pk=price_data['currency_id'])
            price = Price.objects.create(currency=curr, basePrice=price_data['basePrice'],
                                             extraPersonFee = price_data['extraPersonFee'],breakfastFee = price_data['breakfastFee'])
            instance.price = price

        instance.save()
        return instance


class ListingAddressSerializer(serializers.ModelSerializer):
    full = serializers.CharField(source='address.full',help_text='full address',required=False)
    lng = serializers.FloatField(source='address.lng', help_text='map x localization',required=False)
    lat = serializers.FloatField(source='address.lat',help_text='map y localization',required=False)
    street = serializers.CharField(source='address.street', help_text='street',required=False)
    city = serializers.CharField(source='address.city', help_text='city',required=False)
    country = serializers.CharField(source='address.country',help_text='country',required=False)

    class Meta:
        model = Listing
        fields = ('full', 'lng','lat','street','city','country')

    def update(self, instance, validated_data):
        address_data = validated_data['address']
        if instance.address:
            AddressSerializer.update(AddressSerializer(),instance.address,address_data)
        else:
            address = Address.objects.create(city=address_data['city'], country=address_data['country'],
                                             street = address_data['street'],full = address_data['full'],
                                             lat=address_data['lat'],lng=address_data['lng'])
            instance.address = address

        instance.save()
        return instance


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


class ListingGeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = (
         'pk','publicName', 'nickname', 'accommodates', 'bedrooms', 'beds', 'checkInTime', 'checkOutTime', 'propertyType', 'roomType', 'description')


class ListingGetSerializer(serializers.ModelSerializer):
    address = AddressSerializer(help_text='Address of this listing')
    price = PriceSerializer(help_text='Price of this listing')
    extraFee = serializers.FloatField(source='price.currency.extraPersonFee', read_only=True)
    minNights = serializers.IntegerField(read_only=True, source='terms.minNights')
    maxNights = serializers.IntegerField(read_only=True, source='terms.maxNights')

    class Meta:
        model = Listing
        fields = (
         'pk','publicName', 'nickname', 'accommodates', 'bedrooms', 'beds', 'checkInTime', 'checkOutTime', 'propertyType', 'roomType','address'
        ,'price','minNights','maxNights','extraFee','isActive','description')


class ListingPicturesSerializer(serializers.ModelSerializer):
    gallery = PictureSerializer(many=True)
    class Meta:
        model = Listing
        fields = ('gallery',)





