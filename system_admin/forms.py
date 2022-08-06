from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, City, Hotel, PaymentMethod, Feature, ContactUs


# user camelCase for class names
class OurUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'password1', 'password2','role', 'username']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['profile_picture', 'phone_number', 'email', 'username', 'first_name', 'last_name']


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'region']


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'number_of_room', 'city','absolute_location','relative_location', 'picture', 'description', 'feature' ]


class PaymentMethodForm(ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['name', 'type', 'shortcode', 'company_logo', 'description', 'contact']


class FeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = ['type', 'name', 'description']


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'hotel_name', 'phone_number','email']

