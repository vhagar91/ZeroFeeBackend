from django.conf.urls import url, include
from .views import *

# Wire up our API using automatic URL routing.
urlpatterns = [
   url(r'^list/$', ListingViewList.as_view(serializer_class=ListingSerializer),name='listings-list'),
   url(r'^listing/(?P<pk>\d+)/$', ListingGet.as_view(serializer_class=ListingGetSerializer)),
   url(r'^create/$', ListingViewCreate.as_view(serializer_class=ListingSerializer), name='listings-create'),
   url(r'^terms/(?P<pk>\d+)/$', TermsUpdateorCreate.as_view(serializer_class=ListingTermsSerializer)),
   url(r'^address/(?P<pk>\d+)/$', AddressUpdateorCreate.as_view(serializer_class=ListingAddressSerializer)),
   url(r'^general/(?P<pk>\d+)/$', ListingGeneralUpdate.as_view(serializer_class=ListingGeneralSerializer)),
   url(r'^prices/(?P<pk>\d+)/$', ListingPriceUpdate.as_view(serializer_class=ListingPriceSerializer)),
   url(r'^gallery/(?P<pk>\d+)/$', ListingPictures.as_view(serializer_class=ListingPicturesSerializer)),
   url(r'^add-picture/(?P<pk>\d+)/$', CreateListingPicture.as_view(serializer_class=PictureSerializer)),
   url(r'^update-picture/(?P<pk>\d+)/$', UpdateListingPicture.as_view(serializer_class=PictureSerializer)),
   url(r'^delete-picture/(?P<pk>\d+)/$', DeleteListingPicture.as_view(serializer_class=PictureSerializer)),

]