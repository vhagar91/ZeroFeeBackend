from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .utils import asset_upload
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.




class Picture(models.Model):
    thumbnail = models.ImageField(upload_to=asset_upload, null=True, blank=True)
    normal = models.ImageField(upload_to=asset_upload, null=True, blank=True)


class UserProfile(models.Model):
    GENDER_UNKNOWN = 'U'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_UNKNOWN, _('unknown')),
        (GENDER_MALE, _('male')),
        (GENDER_FEMALE, _('female')),
    )
    user = models.OneToOneField(User,unique=True,null=True, on_delete=models.CASCADE)
    gender = models.CharField(_('gender'),null=True, max_length=1, choices=GENDER_CHOICES, default=GENDER_UNKNOWN,help_text=_(
            'The gender of the user Female or Male.'
        ))

    picture = models.OneToOneField(Picture, verbose_name=_('picture'),
                                   help_text=_(
                                       'User Avatar and Picture'
                                   ),
                                   unique=True, on_delete=models.CASCADE, blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)


class Email(models.Model):
    profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=1)
    email = models.EmailField();