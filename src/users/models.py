from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from src.core.models import Picture
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    GENDER_UNKNOWN = 'U'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_UNKNOWN, _('unknown')),
        (GENDER_MALE, _('male')),
        (GENDER_FEMALE, _('female')),
    )
    user = models.OneToOneField(User,unique=True, null=True, on_delete=models.CASCADE)
    gender = models.CharField(_('gender'),null=True, max_length=1, choices=GENDER_CHOICES, default=GENDER_UNKNOWN,help_text=_(
            'The gender of the user Female or Male.'
        ))

    picture = models.OneToOneField(Picture,unique=True, null=True, on_delete=models.CASCADE, help_text=_(
                                       'User Avatar and Picture'
                                   ))
    address = models.CharField(null=True, max_length=50, default='', help_text= 'Users Current Address')
    city = models.CharField(null=True, max_length=20, default='', help_text='Users Current City')
    country = models.CharField(null=True, max_length=20, default='', help_text='Users Current Country')
    about_me = models.CharField(null=True, max_length=30, default='', help_text='Users Extra Info')
    phone = models.CharField(null=True,max_length=50, help_text='Phone number',default='')
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)


