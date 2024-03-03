from django.contrib import admin
from django.urls import path
from Authors import views
urlpatterns=[
    path("AuthorList/",views.AuthorList),
]

