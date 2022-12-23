from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

from blog.models import Blog

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=10, min_length=3)
    password = forms.CharField(max_length=10, min_length=4, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=10, min_length=4, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password", "confirm_password")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control px-3 py-3',
                                                     'placeholder': 'Имя пользователя'})
        self.fields['password'].widget.attrs.update({'class': 'form-control px-3 py-3',
                                                     'placeholder': 'Придумайте пароль'})
        self.fields['confirm_password'].widget.attrs.update({'class': 'form-control px-3 py-3',
                                                             'placeholder': 'Повторите пароль'})

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            return password
        raise ValidationError("Пароли должны совпадать!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


