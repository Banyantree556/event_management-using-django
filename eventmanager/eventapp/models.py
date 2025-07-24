from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class Event(models.Model):
    img=models.ImageField(upload_to='pic/')
    name= models.CharField(max_length=50)
    desc=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_ph=models.CharField(max_length=12)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.cus_name




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
