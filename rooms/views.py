from django.views import generic

from rooms.models import Room, Message


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
    context_object_name = "message"
