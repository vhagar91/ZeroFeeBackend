"""zeroAppBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
)
from src.users.serializers import CustomJWTSerializer
from src.users.views import ObtainJSONWebToken

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/login/$', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    # url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^api/', include('src.urls')),

]
