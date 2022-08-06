from django.db import models
from django_softdelete.models import SoftDeleteModel

from system_admin.models import PaymentMethod, Hotel, Feature, User


# Create your models here.


class Room(SoftDeleteModel,models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, default="Normal")
    Feature = models.ManyToManyField(Feature, blank=True)
    price = models.FloatField()
    number_of_bed = models.IntegerField()
    number_of_room = models.IntegerField()
    picture = models.ImageField(null=True)

    def __str__(self):
        return self.type


class PaymentInformation(SoftDeleteModel,models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    account_holder = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    verified = models.BooleanField(default=False, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.account_number


class ContactAdmin(SoftDeleteModel,models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.message


'''as soon as the admin clicked the message the chat will be created and seen bool set to true'''


class Chat(SoftDeleteModel,models.Model):
    cantact_admin = models.ForeignKey(ContactAdmin, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')


class Message(SoftDeleteModel,models.Model ):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.body
