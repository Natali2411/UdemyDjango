from django.conf.urls import url, include
from UdemyApp import views
from django.urls import path

# Template urls

app_name = "UdemyApp"

urlpatterns = [
    url('^register/$', views.register, name='register'),
]