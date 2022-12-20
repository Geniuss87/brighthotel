from django import forms

from rooms.models import Message


# class MessageForm(forms.Form):
#     name = forms.CharField(max_length=50, min_length=1)
#     email = forms.CharField(max_length=50, min_length=1)
#     subject = forms.CharField(max_length=50, min_length=1)
#     msg = forms.CharField(min_length=1)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

