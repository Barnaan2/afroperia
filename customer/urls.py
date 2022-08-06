from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mybooking/', views.my_booking, name='mybooking'),
    path('contact_us/', views.contact, name='contact_us'),
    path('profile/', views.profile, name='profile'),
    path('selected-hotel', views.selected_hotel, name='selected-hotel'),
    path('pay/<str:id>/', views.pay, name='pay'),
    path('pay/payment_detail/<str:br_id>/<str:pi_id>/', views.payment_detail, name='payment_detail')

]
