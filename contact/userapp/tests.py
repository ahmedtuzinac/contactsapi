#django-rest imports
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token



class TestUserRegistration(APITestCase):


    def test_register(self):

        url = reverse("register")
        data = {
            "username":"testcase",
            "password":"testcasepassword"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class TestUserLoginLogout(APITestCase):
    

    def setUp(self):

        self.user = User.objects.create_user(username="testLogin",
                                             password="password")
        self.token = Token.objects.get(user=self.user)


    def test_login(self):
        
        url = reverse("login")
        data = {
            "username":"testLogin",
            "password":"password"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_logout(self):

        url = reverse("logout")
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    


        
        
    



    
        



