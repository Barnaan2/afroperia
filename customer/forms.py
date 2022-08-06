from django.forms import ModelForm
from .models import Review, BookingRequest, Paid


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'review']


class BookingRequestForm(ModelForm):
    class Meta:
        model = BookingRequest
        fields = [
            'check_in_date', 'check_out_date'
        ]


class PaidForm(ModelForm):
    class Meta:
        model = Paid
        fields = [
            'name','amount', 'transaction_id', 'picture'
        ]
