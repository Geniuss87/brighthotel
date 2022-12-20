from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from rooms.forms import MessageForm
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
    form_class = MessageForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("index")

# def send_msg(request):
#     form = MessageForm(request.POST or None)
#     if form.is_valid():
#         data = form.cleaned_data
#         Message.objects.create(name=data.get("name"),
#                                email=data.get("email"),
#                                subject=data.get("subject"),
#                                msg=data.get("msg"))
#         return redirect("index")
#     return render(request, "contact.html", locals())
