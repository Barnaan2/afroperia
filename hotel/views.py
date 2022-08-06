from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from customer.models import BookingRequest, RequestedRoom, Paid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from hotel.forms import RoomForm, PaymentInformationForm

from hotel.models import Room, ContactAdmin, Chat, Message
from system_admin.models import User
from system_admin.forms import UserForm
from .decorators import allowed_users
from datetime import date


# ------------------------------------------------------------------------------------------------------|
#                                                                                                       |
#   HOTEL INDEX
# ------------------------------------------------------------------------------------------------------|
@never_cache
@login_required(login_url='login')
@allowed_users
def index(request):
    hotel = request.user.hotel_set.all().first()
    booking_requests = BookingRequest.objects.filter(hotel=hotel)
    # the booking requests should be deleted from this reqeustedroom too also they have to be deleted first.
    context = {'booking_requests': booking_requests}
    return render(request, 'hotel/index.html', context)


# ------------------------------------------------------------------------------------------------------|
#                                                                                                       |
# MANAGE ROOM
# ------------------------------------------------------------------------------------------------------|
@login_required(login_url='login')
@allowed_users
def manage_room(request):
    hotel = request.user.hotel_set.all().first()
    rooms = Room.objects.filter(hotel=hotel)
    context = {'rooms': rooms}
    return render(request, 'hotel/manage_room.html', context)


@login_required(login_url='login')
@allowed_users
def add_room(request):
    form = RoomForm()
    hotel = request.user.hotel_set.all().first()
    rooms = Room.objects.filter(hotel=hotel)
    total_room = 0
    for room in rooms:
        total_room += room.number_of_room
    if request.method == "POST":
        total_room += int(request.POST.get('number_of_room'))
        if total_room > hotel.number_of_room:
            messages.error(request, 'there is not enough rooms in your hotel')
            return redirect('hotel')
        else:
            form = RoomForm(request.POST,request.FILES )
            if form.is_valid():
                room = form.save(commit=False)
                room.hotel = hotel
                room.save()
                return redirect('hotel')
            else:
                messages.error(request, 'there is error in your input try again')
    context = {'form': form}
    return render(request, 'hotel/addroom.html', context)


@login_required(login_url='login')
@allowed_users
def edit_room(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            # success message
            messages.success(request, ' updated successfully')
            return redirect('hotel')
    context = {'room': room, 'form': form}
    return render(request, 'hotel/edit_room.html', context)


# ------------------------------------------------------------------------------------------------------|
#                                                                                                       |
# MANAGE PROFILE
# ------------------------------------------------------------------------------------------------------|

# fields = ['profile_picture', 'phone_number', 'email', 'username', 'first_name', 'last_name']
@login_required(login_url='login')
@allowed_users
def profile(request):
    form = User.objects.get(id=request.user.id)
    context = {'form': form}
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('hotel')
    return render(request, 'hotel/profile.html', context)


# ------------------------------------------------------------------------------------------------------|
#                                                                                                       |
# MANAGE CUSTOMER REQUESTS
# ------------------------------------------------------------------------------------------------------|
@login_required(login_url='login')
@allowed_users
def customer_request(request):
    hotel = request.user.hotel_set.all().first()
    booking_requests = BookingRequest.objects.filter(hotel=hotel)
    booking = RequestedRoom.objects.filter(room__hotel=hotel)
    price = price_calculator(booking)

    context = {'booking_requests': booking_requests, 'number_of_rooms': booking, 'price': price}
    return render(request, 'hotel/request.html', context)


@login_required(login_url='login')
@allowed_users
def request_detail(request, id):
    booking_request = BookingRequest.objects.get(id=id)
    q = None
    detail = None

    if request.GET.get('q') is not None:
        q = request.GET.get('q')
        if q == 'paid':
            detail = Paid.objects.get(booking_request=booking_request)
        else:
            if q == 'accept':
                booking_request.status = 'make payment'
                booking_request.save()
                return redirect('hotel')
            elif q == 'cancel':
                booking_request.status = 'cancelled'
                booking_request.save()
                return redirect('hotel')
            else:
                return HttpResponse('404 PAGE NOT FOUND')

    context = {'detail': detail}
    if request.method == 'POST':
        booking_request.status = request.POST['approve']
        booking_request.save()
        return redirect('hotel')
    return render(request, 'hotel/request_detail.html', context)


# ------------------------------------------------------------------------------------------------------|
#                                                                                                       |
# MANAGE PAYMENT INFORMATION
# ------------------------------------------------------------------------------------------------------|
@login_required(login_url='login')
@allowed_users
def add_payment_information(request):
    form = PaymentInformationForm()
    hotel = request.user.hotel_set.all().first()
    if request.method == 'POST':
        form = PaymentInformationForm(request.POST)
        if form.is_valid():
            payment_info = form.save(commit=False)
            payment_info.user = request.user
            payment_info.hotel = hotel
            payment_info.save()
            messages.success(request, 'the operation is done successfully')
            return redirect('hotel')
        else:
            messages.error(request, 'There is an error in your input')
            return redirect('hotel')
    context = {'form': form}
    return render(request, 'hotel/add_payment_information.html', context)


def contact_admin(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        user = request.user
        ContactAdmin.objects.create(user=user, message=message)
        messages.success(request, 'you have sent your message to admins successfully ')
        return redirect('hotel')


# ------------------------------------------------------------------------------------------------------|
#                                                                                                       |
# METHODS FOR SPECIAL PURPOSES
# ------------------------------------------------------------------------------------------------------|
def price_calculator(booking):
    price = []
    price1 = []
    for item in booking:
        check_in = date(item.booking_request.check_in_date.year, item.booking_request.check_in_date.month,
                        item.booking_request.check_in_date.day)
        check_out = date(item.booking_request.check_out_date.year, item.booking_request.check_out_date.month,
                         item.booking_request.check_out_date.day)
        delta = check_out - check_in
        night = delta.days
        total = item.room.price * item.number_of_room * night
        total_price = {'id': item.booking_request.id, 'price': total}
        price.append(total_price)

    yes = 0
    for item in booking:
        for obj in price:
            if obj['id'] == item.booking_request.id:
                yes = yes + obj['price']
        total_price1 = {'id': item.booking_request.id, 'price': yes}
        for objs in price1:
            if objs['id'] == total_price1['id']:
                break
        else:
            price1.append(total_price1)
            yes = 0
    return price1


def booking_request_handler():
    booking_requests = BookingRequest.objects.all()
    for booking_request in booking_requests:
        check_out = date(booking_request.check_out_date.year, booking_request.check_out_date.month,
                         booking_request.check_out_date.day)
        if check_out <= date.today():
            booking_request.status = "expired"
            booking_request.delete()


def chat(request):
    chats = Chat.objects.filter(cantact_admin__user=request.user)
    q = None
    all_message = None
    page = 'hotel'
    if request.GET.get('q') is not None:
        q = request.GET.get('q')
        chat = Chat.objects.get(id=q)
        all_message = Message.objects.filter(chat=chat)
        print(all_message)
    context = {'chats': chats, 'all_message': all_message, 'page': page}
    return render(request, 'chat.html', context)
