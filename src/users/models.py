from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .utils import asset_upload
# Create your models here.


class Email(models.Model):
    email = models.EmailField();


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
    user = models.OneToOneField(User,unique=True, on_delete=models.CASCADE)
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES, default=GENDER_UNKNOWN, null=True)
    emails = models.ManyToManyField(
        Email,
        verbose_name=_('emails'),
        blank=True,
        help_text=_(
            'The emails this user has configured.'
        ),
        related_name="email_set",
        related_query_name="user_profile",
    )
    picture = models.OneToOneField(Picture,unique=True, on_delete=models.CASCADE,blank=True)


