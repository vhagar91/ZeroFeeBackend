from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from zeroAppBackend.permisions import OnlyAPIPermission
from .models import Listing
from .serializers import ListingSerializer, ListingTermsSerializer , ListingGeneralSerializer, ListingAddressSerializer
from ..utils.custom_pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ListingFilter
# Create your views here.


class ListingViewList(ListAPIView):
    """
    API endpoint that allows list of Listings.
    """
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ListingFilter


class ListingViewCreate(CreateAPIView):
    """
    API endpoint that allows create a Listing.
    """
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class TermsUpdateorCreate(RetrieveUpdateAPIView):
    """
    API endpoint that allows update a Terms.
    """
    # permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingTermsSerializer
    lookup_field = 'pk'


class AddressUpdateorCreate(RetrieveUpdateAPIView):
    """
    API endpoint that allows update a Address.
    """
    # permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingAddressSerializer
    lookup_field = 'pk'


class ListingGeneralUpdate(UpdateAPIView):
    """
    API endpoint that allows update a General Data.
    """
    # permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingGeneralSerializer
    lookup_field = 'pk'

