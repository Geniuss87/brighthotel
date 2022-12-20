from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm

User = get_user_model()


class RegisterUserView(generic.CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "auth/register.html"

    def get_success_url(self):
        return reverse_lazy("index")
