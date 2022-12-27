from django.contrib import admin
from rooms.models import Room, Image, Message, Booking

admin.site.register(Room)
admin.site.register(Image)
admin.site.register(Message)
admin.site.register(Booking)