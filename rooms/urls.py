from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rooms/', views.RoomsView.as_view(), name='rooms'),
    path('rooms/booking/<int:pk>/', views.BookingRoomSingleView.as_view(), name='booking'),
    path('rooms/room_single/<int:pk>/', views.RoomSingleView.as_view(), name='room_single'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('booking-room/', views.BookingRoomView.as_view(), name='booking_room'),
    path('booking_single/', views.BookingCreateView.as_view(), name='booking_single'),
]
