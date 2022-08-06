from django.forms import ModelForm

from hotel.models import Room, PaymentInformation, ContactAdmin


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['type', 'number_of_room', 'number_of_bed', 'price', 'Feature', 'picture']


class PaymentInformationForm(ModelForm):
    class Meta:
        model = PaymentInformation
        fields = ['payment_method', 'account_holder', 'account_number', 'phone_number']


class ContactAdminForm(ModelForm):
    class Meta:
        model = ContactAdmin
        fields = ['message']
