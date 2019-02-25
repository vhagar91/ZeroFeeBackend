from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProfileSerializer, PictureSerializer
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,UpdateAPIView
from ..utils.custom_pagination import CustomPagination
from zeroAppBackend.permisions import OnlyAPIPermission
from .models import Picture
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.registration.views import LoginView
from rest_framework.authentication import TokenAuthentication

class LoginViewCustom(LoginView):
    authentication_classes = (TokenAuthentication,)

class FacebookLogin(SocialLoginView):

    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class UserViewList(ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter


class AddUserView(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser, OnlyAPIPermission)
    queryset = User.objects.all();
    serializer_class = UserSerializer;


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class ProfileViewGet(RetrieveUpdateAPIView):
    """
       API endpoint that allows obtain a User Profile.
       """
    permission_classes = (IsAuthenticated, OnlyAPIPermission)
    serializer_class = ProfileSerializer
    lookup_field = 'pk'
    queryset = User.objects.all()


class ProfilePictureUpdate(UpdateAPIView):
    """
       API endpoint that update Users Profile Picture
       """
    permission_classes = (IsAuthenticated, OnlyAPIPermission)
    serializer_class = PictureSerializer
    lookup_field = 'pk'
    queryset = Picture.objects.all()



