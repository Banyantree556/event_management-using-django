from django.contrib import admin
from .models import Event,Booking

# Register your models here.
admin.site.register(Event)
admin.site.register(Booking)

from .models import UserProfile

admin.site.register(UserProfile)

