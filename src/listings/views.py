from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from zeroAppBackend.permisions import OnlyAPIPermission
from .models import Listing, PictureListing
from .serializers import PictureSerializer,ListingPicturesSerializer, ListingPriceSerializer, ListingSerializer, ListingTermsSerializer , ListingGeneralSerializer, ListingAddressSerializer, ListingGetSerializer
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
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingTermsSerializer
    lookup_field = 'pk'


class AddressUpdateorCreate(UpdateAPIView):
    """
    API endpoint that allows update a Address.
    """
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingAddressSerializer
    lookup_field = 'pk'


class ListingGeneralUpdate(UpdateAPIView):
    """
    API endpoint that allows update a General Data.
    """
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingGeneralSerializer
    lookup_field = 'pk'


class ListingPriceUpdate(UpdateAPIView):
    """
    API endpoint that allows update a General Data.
    """
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingPriceSerializer
    lookup_field = 'pk'


class ListingGet(RetrieveAPIView):
    """
    API endpoint that allows to get a Listing.
    """
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingGetSerializer
    lookup_field = 'pk'


class ListingPictures(RetrieveAPIView):
    """
    API endpoint that allows to get the Listing Gallery.
    """
    permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = Listing.objects.all()
    serializer_class = ListingPicturesSerializer
    lookup_field = 'pk'


class CreateListingPicture(CreateAPIView):
    """
    API endpoint that allows to Put a Listing Picture.
    """
    # permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = PictureListing.objects.all()
    serializer_class = PictureSerializer
    lookup_field = 'pk'


class UpdateListingPicture(UpdateAPIView):
    """
    API endpoint that allows to Put a Listing Picture.
    """
    # permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = PictureListing.objects.all()
    serializer_class = PictureSerializer
    lookup_field = 'pk'


class DeleteListingPicture(DestroyAPIView):
    """
    API endpoint that allows to Put a Listing Picture.
    """
    # permission_classes = (IsAuthenticated,IsAdminUser,OnlyAPIPermission)
    queryset = PictureListing.objects.all()
    serializer_class = PictureSerializer
    lookup_field = 'pk'