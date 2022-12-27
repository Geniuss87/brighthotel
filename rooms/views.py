from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic, View

from rooms.forms import MessageForm, BookingForm
from rooms.models import Room, Message, Booking


class IndexView(generic.TemplateView):
    template_name = "index.html"


class RoomsView(generic.ListView):
    model = Room
    template_name = "rooms.html"
    context_object_name = "rooms"

    def get_queryset(self):
        queryset = Room.objects.all().order_by('id')
        return queryset


class RoomSingleView(generic.DetailView):
    model = Room
    template_name = "room-single.html"
    context_object_name = "room"


class ServicesView(generic.TemplateView):
    template_name = "services.html"


class AboutView(generic.TemplateView):
    template_name = "about.html"


class ContactView(generic.CreateView):
    model = Message
    template_name = "contact.html"
    form_class = MessageForm

    def get_success_url(self):
        return reverse_lazy("index")


class BookingRoomView(View):
    def post(self, request):
        data = request.POST
        checkin = data["checkin_date"]
        checkout = data["checkout_date"]
        free_rooms = Booking.objects.filter(
            checkin__lte=checkin,
            checkout__gt=checkin
        ).values_list("room__id")
        rooms = Room.objects.exclude(id__in=free_rooms).order_by("id")
        return render(request, "rooms.html", context={"rooms": rooms, "checkin": checkin, "checkout": checkout})


class BookingRoomSingleView(generic.DetailView):
    model = Room
    template_name = "booking.html"
    context_object_name = "room"


class BookingCreateView(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking.html"

    def get_success_url(self):
        return reverse_lazy('index')


