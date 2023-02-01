from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from contactsapp.models import Contact
from contactsapp.serializers import ContactSerializer
from contactsapp.permissions import IsValidUser
# Create your views here.

class ContactList(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields  = ['name'] 
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend
    ]      
    search_fields = [
        'name',
        'phonenumber'
    ]
    #part where is implementet searching by name and phonenumber
    #in url we are adding ?search=VALUE and it's searching names and phonenumbers 

    def get_queryset(self):
        contacts = Contact.objects.filter(user=self.request.user).select_related("user")
        return contacts


class ContactDetail(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsValidUser]
    http_method_names = ["get","put","delete"]

    def get_queryset(self):
        contacts = Contact.objects.filter(user=self.request.user).select_related("user")
        return contacts