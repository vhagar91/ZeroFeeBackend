from django.conf.urls import url, include
from rest_framework import routers
from src.users import views
from .serializers import UserSerializer,ProfileSerializer, PictureSerializer
from .views import UserViewList, ProfileViewGet, ProfilePictureUpdate
# router = routers.DefaultRouter()
# router.register(r'list', views.UserViewList)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
   url(r'^list/$', UserViewList.as_view(serializer_class=UserSerializer),name='users-list'),
   url(r'^profile/(?P<pk>\d+)/$', ProfileViewGet.as_view(serializer_class=ProfileSerializer)),
   url(r'^avatar/(?P<pk>\d+)/$', ProfilePictureUpdate.as_view(serializer_class=PictureSerializer)),

]