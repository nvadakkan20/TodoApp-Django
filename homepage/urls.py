from django.urls import path
from homepage import views as home

urlpatterns = [
    path("", home.homepage, name='home'),
]