from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from src.core.models import Address, Picture


# Create your models here.
class Price (models.Model):
    currency = models.CharField(max_length=200,null=False, help_text='Base currency')
    basePrice = models.IntegerField(null=False,default=0,help_text='Base Price')
    extraPersonFee = models.IntegerField(null=False,default=0,help_text='Extra person Fee')


class Terms (models.Model):
    minNights = models.IntegerField(null=False,default=1,help_text='Min Nights Allow')
    maxNights = models.IntegerField(null=False,default=45,help_text='Max Nights Allow')


class Listing (models.Model):
    PROPERTY_TYPE_UNKNNOWN = 0
    PROPERTY_TYPE_APARTMENT = 1
    PROPERTY_TYPE_HOME = 2
    PROPERTY_TYPE_VILLA = 3
    PROPERTY_TYPE_PENTHOUSE = 4
    PROPERTY_TYPE_CHOICES = (
        (PROPERTY_TYPE_UNKNNOWN, _('unknown')),
        (PROPERTY_TYPE_APARTMENT, _('Apartment')),
        (PROPERTY_TYPE_HOME,_('Home')),
        (PROPERTY_TYPE_VILLA,_('Villa')),
        (PROPERTY_TYPE_PENTHOUSE,_('Penthouse'))
    )
    ROOM_TYPE_UNKNOWN = 0
    ROOM_TYPE_FULL_PROPERTY = 1
    ROOM_TYPE_ROOM = 2
    ROOM_TYPE_CHOICES = (
        (ROOM_TYPE_UNKNOWN, _('unknown')),
        (ROOM_TYPE_FULL_PROPERTY, _('Full Property')),
        (ROOM_TYPE_ROOM, _('Room')),
    )
    accommodates = models.IntegerField(default=0, help_text ='How many people cant host the listing')
    bedrooms = models.IntegerField(default=0, help_text='How many rooms the listing have')
    beds = models.IntegerField(default=0, help_text='How many Beds the listing have')
    checkInTime = models.TimeField(null=True, help_text='Time for checkIn at the listing')
    checkOutTime = models.TimeField(null=True, help_text='Time for chekOut at the listing')
    propertyType = models.IntegerField(null=False, choices=PROPERTY_TYPE_CHOICES,default=PROPERTY_TYPE_UNKNNOWN,
                                    help_text='Property Type')
    roomType = models.IntegerField(null=False, choices=ROOM_TYPE_CHOICES, default=ROOM_TYPE_UNKNOWN, help_text='Room Type Full Property/Room')
    owner = models.OneToOneField(User, unique=True, null=True, on_delete=models.CASCADE,
                                 help_text='Owner of the listing')
    nickname = models.CharField(null=False, default='Nickname', max_length=200, help_text='Listing Nickname')
    address = models.OneToOneField(Address,null=True,on_delete=models.CASCADE, help_text='Listing Address')
    createAt = models.DateTimeField(auto_now=True, help_text='Date of creation')
    isActive = models.BooleanField(default=False, help_text='Is the listing active or not')
    picture = models.OneToOneField(Picture, unique=True, null=True, on_delete=models.CASCADE, help_text=_(
        'Main listing Picture'
    ))
    pictures = models.ManyToManyField(Picture,related_name='pictures',help_text='Pictures Gallery')
    price = models.OneToOneField(Price,unique=True,null=True,on_delete=models.CASCADE, help_text='listing prices')
    terms = models.OneToOneField(Terms,unique=True,null=True,on_delete=models.CASCADE, help_text='listing min and max stay allowed')
