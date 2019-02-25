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
from src.users.views import FacebookLogin, GoogleLogin
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import refresh_jwt_token
from src.users.views import LoginViewCustom
urlpatterns = [
    path('admin/', admin.site.urls),
    # Generate schema with valid `request` instance:
    url(r'^docs/', include_docs_urls(title='Zero Fee API', public=False)),
    url(r'^rest-auth/login/$', LoginViewCustom.as_view(), name='rest_login'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/refresh/', refresh_jwt_token),
    # url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/', include('src.urls')),



]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
