from rest_framework.serializers import ModelSerializer
from contactsapp.models import Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        exclude = ['user',]


    def create(self, validated_data):

        contact = Contact.objects.create(
            user = self.context["request"].user, 
            name = validated_data["name"],
            phonenumber = validated_data["phonenumber"],
            email = validated_data["email"]
        )
        return contact


