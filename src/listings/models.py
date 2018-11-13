from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from src.core.models import Currency
from src.core.utils import asset_upload_property


class Address(models.Model):
    full = models.CharField(max_length=250, null=True, help_text='Full address')
    lng = models.FloatField(help_text='Geo Longitude',null=True)
    lat = models.FloatField(help_text='Geo Latitude',null=True)
    street = models.CharField(max_length=200,null=True,help_text='Street')
    city = models.CharField(max_length=200,null=True,help_text='City')
    country = models.CharField(max_length=200,null=True,help_text='Country')


class PictureListing(models.Model):
    thumbnail = models.ImageField(upload_to=asset_upload_property, null=True, blank=True)
    normal = models.ImageField(upload_to=asset_upload_property, null=True, blank=True)


# Create your models here.
class Price (models.Model):
    currency = models.OneToOneField(Currency,unique=True, null=False, help_text='Base currency',on_delete=models.CASCADE)
    basePrice = models.IntegerField(null=False,default=0, help_text='Base Price')
    extraPersonFee = models.IntegerField(null=False,default=0, help_text='Extra person Fee')
    breakfastFee = models.IntegerField(null=True, help_text='breakfast fee')


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
    propertyType = models.IntegerField(null=True, choices=PROPERTY_TYPE_CHOICES,default=PROPERTY_TYPE_UNKNNOWN,
                                    help_text='Property Type')
    roomType = models.IntegerField(null=True, choices=ROOM_TYPE_CHOICES, default=ROOM_TYPE_UNKNOWN, help_text='Room Type Full Property/Room')
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    nickname = models.CharField(null=False, default='Nickname', max_length=200, help_text='Listing Nickname')
    publicName = models.CharField(null=False, default='Nickname', max_length=200, help_text='Listing Nickname')
    address = models.OneToOneField(Address,null=True,on_delete=models.CASCADE, help_text='Listing Address')
    createAt = models.DateTimeField(auto_now=True, help_text='Date of creation')
    isActive = models.BooleanField(default=False, help_text='Is the listing active or not')
    picture = models.OneToOneField(PictureListing, unique=True, null=True, on_delete=models.CASCADE, help_text=_(
        'Main listing Picture'
    ))
    pictures = models.ManyToManyField(PictureListing,related_name='pictures',help_text='Pictures Gallery')
    price = models.OneToOneField(Price,unique=True,null=True,on_delete=models.CASCADE, help_text='listing prices')
    terms = models.OneToOneField(Terms,unique=True,null=True,on_delete=models.CASCADE, help_text='listing min and max stay allowed')


class Reservation (models.Model):
    STATUS_TYPE_inquiry = 0
    STATUS_TYPE_declined = 1
    STATUS_TYPE_expired = 2
    STATUS_TYPE_canceled = 3
    STATUS_TYPE_reserved = 4
    STATUS_TYPE_confirmed = 5
    STATUS_TYPE_awaiting_payment = 6
    STATUS_TYPE_CHOICES = (
        (STATUS_TYPE_inquiry, _('inquiry')),
        (STATUS_TYPE_declined, _('declined')),
        (STATUS_TYPE_expired, _('expired')),
        (STATUS_TYPE_canceled, _('canceled')),
        (STATUS_TYPE_reserved, _('reserved')),
        (STATUS_TYPE_confirmed, _('confirmed')),
        (STATUS_TYPE_awaiting_payment, _('Awaiting for Payment')),

    )
    listing = models.OneToOneField(Listing,null=True,unique=True,on_delete=models.CASCADE, help_text='listing booked')
    createdAt = models.DateField(auto_now=True,help_text='Day of creations',null=True)
    lastUpdatedAt = models.DateField(auto_now=True,null=True,help_text='Last updated Day')
    confirmationCode = models.CharField(max_length=50,null=True,help_text=('Confirmation Code exp C001'))
    checkIn = models.DateField(null=True,help_text='Day of entrance')
    checkOut = models.DateField(null=True,help_text='Day leaving the listing')
    nightsCount = models.IntegerField(null=True,help_text='Amount of nights')
    daysInAdvance = models.IntegerField(null=True,help_text='Days in Advance of the booking')
    guestsCount = models.IntegerField(null=True,help_text='Amount of guest to recieve')
    status = models.IntegerField(null=False, choices=STATUS_TYPE_CHOICES,default=STATUS_TYPE_inquiry,
                                    help_text='Status')
    guest = models.OneToOneField(User,null=False,unique=True,on_delete=models.CASCADE,help_text=('reference to de client'))

