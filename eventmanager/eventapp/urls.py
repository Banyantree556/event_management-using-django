from django.urls import path
from . import views
from . views import signup_view
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('events/',views.events,name='events'),
    path('booking/',views.booking,name='booking'),
    path('contact',views.contact,name='contact'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('goodbye/', views.logout_thankyou, name='logout_thankyou'),
     path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'
    ), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),

]