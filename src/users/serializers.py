from django.contrib.auth.models import User, Group
from .models import *
from src.core.models import Picture
from rest_auth.serializers import JWTSerializer
from rest_framework import serializers
from django.dispatch import receiver
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
from django.contrib.auth import get_user_model
import os
UserModel = get_user_model()


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'avatar')
        read_only_fields = ('email',)

    def get_avatar(self, user):
        request = self.context.get('request')
        profile = UserProfile.objects.get(user=user);
        if profile.picture:
            photo_url = profile.picture.thumbnail.url
            return request.build_absolute_uri(photo_url)
        else:
            return ''


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    group = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'groups', 'first_name', 'last_name', 'is_staff', 'password', 'group')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email= validated_data['email'],
            last_name= validated_data['last_name'],
            first_name= validated_data['first_name'],
            is_staff= validated_data['is_staff'])
        users_group = Group.objects.get(name=validated_data['group'])
        user.set_password(validated_data['password'])
        user.save()
        users_group.user_set.add(user)
        return user


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('id', 'thumbnail', 'normal')

    @receiver(models.signals.pre_delete, sender=UserProfile)
    def auto_delete_avatar_on_delete(sender, instance, **kwargs):
        """Deletes file from filesystem
        when corresponding `File` object is deleted.
     """
        if instance._state.adding is False:
            if instance:
                if os.path.isfile(instance.picture):
                    os.remove(instance.picture.thumbnail.path)
                    os.remove(instance.picture.normal.path)


class ProfileSerializer(UserSerializer):
    gender = serializers.CharField(source="userprofile.gender")
    address = serializers.CharField(source="userprofile.address")
    city = serializers.CharField(source="userprofile.city")
    country = serializers.CharField(source="userprofile.country")
    about_me = serializers.CharField(source="userprofile.about_me")
    picture = PictureSerializer(source= 'userprofile.picture')
    phone = serializers.CharField(source='userprofile.phone')

    class Meta(UserSerializer.Meta):
        fields = ('username','email','first_name','last_name', 'gender','picture', 'address', 'city', 'country', 'about_me', 'phone')
        depth = 1

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)
        profile = instance.userprofile
        picture = instance.userprofile.picture
        p_info = model_meta.get_field_info(profile)
        pic_info = model_meta.get_field_info(picture)

        for attr, value in validated_data.items():
            if attr == 'userprofile':
                for attr2, value2 in value.items():
                    if attr2 == 'picture':
                        for attr3, value3 in value2.items():
                            setattr(picture, attr3, value3)
                    else :
                        setattr(profile, attr2, value2)

            elif attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        picture.save()
        profile.save()

        return instance





