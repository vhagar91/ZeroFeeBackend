from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,IsAdminUser)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


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