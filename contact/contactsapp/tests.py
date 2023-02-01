from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from contactsapp.models import Contact

# Create your tests here.


class TestContacts(APITestCase):


    def setUp(self):

        self.user = User.objects.create_user(
            username="TestUserContactsApp",
            password="password"
        )
        self.tokenContact = Token.objects.get(user=self.user)
        self.contact = Contact.objects.create(
            user=self.user,
            name="SetUp User",
            phonenumber="TestPHN",
            email = "test@gmail.com"
        )
        
    
    def test_ContactCreate(self):

        url = reverse("list")
        data = {
            "name":"Test Name",
            "phonenumber":"+PHONENUMBER",
            "email":"test@gmail.com"
        }
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.tokenContact.key)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_ContactList(self):

        url = reverse("list")
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.tokenContact.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_ContactUpdate(self):

        url = f"http://127.0.0.1:8000/contact/{self.contact.id}/"
        data = {
            "name":"Test Name - Updated",
            "phonenumber":"+PHONENUMBER - Updated",
            "email":"test@gmail.com"
        }
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.tokenContact.key)
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_ContactDelete(self):

        url = f"http://127.0.0.1:8000/contact/{self.contact.id}/"
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.tokenContact.key)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    
    
        