from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Event
from .forms import BookingForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import UserProfile
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.utils.safestring import mark_safe

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')
    def form_invalid(self, form):
         msg = mark_safe(
            '❌ Invalid credentials. '
            'Forgot your password? <a href="{0}">Reset it here</a>.'.format(reverse_lazy('password_reset'))
        )
         messages.error(self.request, msg)
         return super().form_invalid(form)
    
def custom_logout(request):
    logout(request)
    return redirect('logout_thankyou') 

def logout_thankyou(request):
    return render(request, 'logout_thankyou.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

           
            profile = user.userprofile
            profile.mobile = form.cleaned_data['mobile']
            profile.place = form.cleaned_data['place']
            profile.pin = form.cleaned_data['pin']
            profile.save()

            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def index(request):
    
    dict_eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'index.html', dict_eve)
#render is used to diaply the content i.e,index.html
def about(request):
    return render(request,"about.html")


def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,"events.html",dict_eve) #we use dictionary (eve) to retrieve data from db


from django.contrib import messages

def booking(request):
    event_id = request.GET.get('event')
    form = BookingForm(initial={'name': event_id}) if event_id else BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['show_success_modal'] = True  
            return redirect('booking')  # redirect back to same page

    # Check and clear modal flag
    show_modal = request.session.pop('show_success_modal', False)

    return render(request, "booking.html", {'form': form, 'show_modal': show_modal})




def contact(request):
    return render(request,"contact.html")

