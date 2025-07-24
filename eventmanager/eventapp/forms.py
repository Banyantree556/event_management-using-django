from django import forms
from django.core.validators import RegexValidator
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    mobile = forms.CharField(max_length=15)
    place = forms.CharField(max_length=100)
    pin = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    cus_name = forms.CharField(
        label="Customer name: ",
        max_length=55,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message="Name must contain only letters and spaces."
            )
        ],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    cus_ph = forms.CharField(
        label="Customer phone number: ",
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^\d{10,11}$',
                message="Phone number must be 10 or 11 digits."
            )
        ],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(attrs={'class': 'form-control'}),
            'name': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'name': "Event name: ",
            'booking_date': "Booking date: ",
        }
