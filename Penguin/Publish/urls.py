from django.contrib import admin
from django.urls import path
from Publish import views

urlpatterns=[
    path("push/",views.push),
]

