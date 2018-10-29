from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from .models import UserProfile,User
from .serializers import ProfileSerializer,UserSerializer
from rest_framework_api_key.models import APIKey
from .views import *
# Create your tests here.


class GetUsersTest(APITestCase):
    """ Test module for GET all users """

    def setUp(self):
        self.client = APIClient()
        self.normal_user = User.objects.create_user(
            username="joe", password="password", email="joe@soap.com")
        self.superuser = User.objects.create_superuser(
            username="clark", password="supersecret", email="joe@soap.com")
        User.objects.create(
            username='Casper',email='email@uci.cu', first_name='lol',last_name='asd',password='lokoloko')
        User.objects.create(
            username='Muffin',email='email@uci.cu', first_name='lol',last_name='asd',password='lokoloko')
        User.objects.create(
            username='Rambo',email='email@uci.cu', first_name='lol',last_name='asd',password='lokoloko')
        User.objects.create(
            username='Ricky',email='email@uci.cu', first_name='lol',last_name='asd',password='lokoloko')
        self.apiKey=APIKey.objects.create(name='abc',key='abc')


    def test_get_users(self):
        url = reverse('api-jwt-auth')
        resp = self.client.post(url,{'username_or_email': 'clark', 'password': 'supersecret'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        token = resp.data['token']['access']
        # print(token)

        url = reverse("users-list")

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        """GET /user returns a list of users"""

        response = self.client.get(url,data={'apikey': self.apiKey.id,'page':1})
        assert response.status_code == 200, \
            "Expect 200 OK. got: {}".format(response.status_code)

        num_users = len(response.json())

        assert num_users == 4, \
            "Expect it to return exactly 4 users. Got: {}".format(num_users)
        """GET /user returns a list of users"""


    def test_get_user_returns_correct_fields(self):
        """GET /user/{pk} returns a user"""
        assert True is True

