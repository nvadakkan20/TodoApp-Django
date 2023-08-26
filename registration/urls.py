from django.urls import path
from registration import views

urlpatterns = [
    path("login/", views.loginPage, name='login'),
    path("signup/", views.signup, name='signup'),
    path("logout/", views.logoutPage, name='logout'),
]