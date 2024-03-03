from django.contrib import admin
from django.urls import path
from About_Us import views

urlpatterns=[
    path('info/',views.info),
]

