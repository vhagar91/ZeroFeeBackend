from django.contrib.auth.models import User, Group
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.utils.six import text_type
from django.dispatch import receiver
import os


class CustomJWTSerializer(TokenObtainPairSerializer):
    username_field = 'username_or_email'

    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(email=attrs.get("username_or_email")).first() or User.objects.filter(username=attrs.get("username_or_email")).first()
        if user_obj is not None:
            credentials = {
                'username':user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = _('User account is disabled.')
                        raise serializers.ValidationError(msg)

                    data = {}
                    token = {}
                    userData = {}
                    refresh = self.get_token(user)

                    token['refresh'] = text_type(refresh)
                    token['access'] = text_type(refresh.access_token)
                    userData['name'] = user_obj.username
                    userData['email'] = user_obj.email
                    userData['id'] = user_obj.id
                    data['token']=token
                    data['user']=userData
                    return data
                else:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg)

            else:
                msg = _('Must include "{username_field}" and "password".')
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = _('Account with this email/username does not exists')
            raise serializers.ValidationError(msg)


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'groups', 'first_name', 'last_name', 'is_staff')


class EmailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Email
        fields = ('email',)


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    photo_url = serializers.SerializerMethodField()
    picture = serializers.SlugRelatedField(slug_field='id', queryset=Picture.objects.all())
    email_set = EmailSerializer(read_only=True,many=True)

    class Meta:
        model = UserProfile
        fields = ('user_id', 'gender', 'email_set', 'photo_url', 'picture')
        depth = 1

    extra_kwargs = {
       'user': {'lookup_field': 'pk'}
    }

    def get_photo_url(self, profile):
        request = self.context.get('request')
        if profile.picture:
           photo_url = profile.picture.thumbnail.url
           return request.build_absolute_uri(photo_url)
        else:
            return ''

    @receiver(models.signals.pre_delete, sender=UserProfile)
    def auto_delete_avatar_on_delete(sender, instance, **kwargs):
        """Deletes file from filesystem
        when corresponding `File` object is deleted.
     """
        if instance._state.adding is False:
            if instance.picture:
                if os.path.isfile(instance.picture.path):
                    os.remove(instance.picture.path)


class AvatarSerializer(serializers.HyperlinkedModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ('photo_url',)

    extra_kwargs = {
        'user': {'lookup_field': 'pk'}
    }

    def get_photo_url(self, profile):
        request = self.context.get('request')
        if profile.picture:
            photo_url = profile.picture.thumbnail.url
            return request.build_absolute_uri(photo_url)
        else:
            return ''
