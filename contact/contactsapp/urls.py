from django.urls import path 
from contactsapp.views import ContactList, ContactDetail

urlpatterns = [
    path("contacts/", ContactList.as_view(), name="list"),
    path("contact/<int:pk>/", ContactDetail.as_view(), name="detail")
]
