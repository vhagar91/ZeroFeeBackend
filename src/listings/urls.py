from django.conf.urls import url, include
from .serializers import ListingSerializer
from .views import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
   url(r'^list/$', ListingViewList.as_view(serializer_class=ListingSerializer),name='listings-list'),


]