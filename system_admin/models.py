from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django_softdelete.models import SoftDeleteModel


class User(AbstractUser,SoftDeleteModel):
    phone_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20)
    profile_picture = models.ImageField(null=True, default="avatar.png")
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []


class City(SoftDeleteModel, models.Model):
    name = models.CharField(max_length=55, unique=True)
    region = models.CharField(max_length=55, null=True)
    country = models.CharField(max_length=55, null=True, default='Ethiopia')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Feature(SoftDeleteModel, models.Model):
    type = models.CharField(max_length=55)
    name = models.CharField(max_length=55, unique=True)
    description = models.TextField(max_length=300, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Hotel(SoftDeleteModel, models.Model):
    name = models.CharField(max_length=50)
    admin = models.ManyToManyField(User, blank=True,)
    number_of_room = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    relative_location = models.TextField()
    absolute_location = models.TextField()
    picture = models.ImageField()
    feature = models.ManyToManyField(Feature, blank=True)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PaymentMethod(SoftDeleteModel, models.Model):
    name = models.CharField(max_length=55, unique=True)
    type = models.CharField(max_length=55)
    shortcode = models.TextField(max_length=20)
    company_logo = models.ImageField(null=True, default='payment_method.png')
    description = models.TextField(max_length=200)
    contact = models.TextField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.name


class ContactUs(SoftDeleteModel, models.Model):
    name = models.CharField(max_length=55)
    hotel_name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=55, unique=True)
    email = models.EmailField(null=True)
    seen = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.hotel_name
