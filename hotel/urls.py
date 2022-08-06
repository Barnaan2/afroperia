from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='hotel'),
    path('manage-room/', views.manage_room, name='manage_room'),
    path('add-room/', views.add_room, name='add_room'),
    path('edit/<str:id>/',views.edit_room,name='edit_room'),
    path('profile/', views.profile, name='hotel_profile'),
    path('request/', views.customer_request, name='request'),
    path('add_payment_information/', views.add_payment_information, name='add_payment_information'),
    path('message/', views.contact_admin, name='contact_admin'),
    path('request_detail/<str:id>/', views.request_detail, name='request_detail'),
    path('Chat/', views.chat, name='hotel-chat'),



]
