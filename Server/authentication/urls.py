from django.contrib import admin
from django.urls import path
from .views import EndUserRegistrationView, AdminRegistrationView, LoginView

urlpatterns = [
    path('user/signup', EndUserRegistrationView.as_view(), name='enduser_registration'),
    path('admin/signup', AdminRegistrationView.as_view(), name='admin_registration'),
    path('login', LoginView.as_view(), name='login'),
]
