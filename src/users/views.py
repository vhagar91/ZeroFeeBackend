from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CustomJWTSerializer, ProfileSerializer, AvatarSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from zeroAppBackend.permisions import OnlyAPIPermission
from rest_framework_api_key.permissions import HasAPIAccess
from .models import UserProfile


class UserViewList(ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ObtainJSONWebToken(TokenObtainPairView):
    """
    API endpoint that allows obtain a JWT.
    """

    serializer_class = CustomJWTSerializer


class ProfileViewGet(RetrieveUpdateAPIView):
    """
       API endpoint that allows obtain a User Profile.
       """
    serializer_class = ProfileSerializer
    lookup_field = 'user'
    queryset = UserProfile.objects.all()


class AvatarViewGet(RetrieveAPIView):
    """
       API endpoint that allows obtain a User Avatar.
       """
    serializer_class = AvatarSerializer
    lookup_field = 'user'
    queryset = UserProfile.objects.all()