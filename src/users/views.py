from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CustomJWTSerializer, ProfileSerializer, PictureSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,UpdateAPIView
from ..utils.custom_pagination import CustomPagination
from zeroAppBackend.permisions import OnlyAPIPermission
from .models import UserProfile , Picture
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend

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
    queryset = User.objects.all();
    serializer_class = UserSerializer;


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



