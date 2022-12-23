from django import forms

from rooms.models import Message, Booking


# class MessageForm(forms.Form):
#     name = forms.CharField(max_length=50, min_length=1, wi)
#     email = forms.CharField(max_length=50, min_length=1)
#     subject = forms.CharField(max_length=50, min_length=1)
#     msg = forms.CharField(min_length=1)

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
