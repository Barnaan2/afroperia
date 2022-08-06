from django.db import models
from django_softdelete.models import SoftDeleteModel

from hotel.models import Hotel, Room, PaymentInformation
from system_admin.models import User


# Create your models here.
class Review(SoftDeleteModel, models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250, null=True)
    review = models.IntegerField()
    hide_identity = models.BooleanField(default=False, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __int__(self):
        return self.review


'''
in many to many relation query if the field is not written the object you are making the query through you 
must use _set  
it also work like any other model
'''


class BookingRequest(SoftDeleteModel, models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    room = models.ManyToManyField(Room, through='RequestedRoom')
    status = models.CharField(max_length=55, default="waiting")
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.status


# the class to represent the many-to-many relation between the room and booking_request
# booking request.room.add(the_room,through_defaults={'number_of_room' : the_number_no_of_room})
class RequestedRoom(SoftDeleteModel, models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    booking_request = models.ForeignKey(BookingRequest, on_delete=models.CASCADE)
    number_of_room = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['booking_request', 'room']]


class Paid(SoftDeleteModel, models.Model):
    payment_information = models.ForeignKey(PaymentInformation, on_delete=models.CASCADE)
    booking_request = models.ForeignKey(BookingRequest, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    transaction_id = models.CharField(max_length=60)
    expected_payment = models.FloatField()
    amount = models.FloatField()
    picture = models.ImageField(null=True, default='payment_method.png')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# this is needed for production but for now let just comment it out.
    class Meta:
        unique_together = [['booking_request', 'transaction_id']]
