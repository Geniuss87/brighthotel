from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=10, min_length=3)
    password_1 = forms.CharField(max_length=10, min_length=4)
    password_2 = forms.CharField(max_length=10, min_length=4)

    class Meta:
        model = User
        fields = ("username", "password_1", "password_2")

    def clean_password_2(self):
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")
        if password_1.isalpha() and password_1 == password_2:
            return password_1
        raise ValidationError("Пароль должен содержать только буквы и должны совпадать!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password_1"])
        if commit:
            user.save()
        return user
