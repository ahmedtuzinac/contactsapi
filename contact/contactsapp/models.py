from django.db.models import (Model, ForeignKey,
                              CharField, EmailField, CASCADE)
from django.contrib.auth.models import User
# Create your models here.


class Contact(Model):

    user = ForeignKey(
        User,
        on_delete = CASCADE,
        related_name = "contacts"
    )
    name = CharField(max_length = 150)
    phonenumber = CharField(max_length = 150)
    email = EmailField(blank = True, null = True)

    def __str__(self):
        return self.name


