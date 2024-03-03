"""
URL configuration for Penguin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Books/",include('Books.urls')),
    path("Authors/",include('Authors.urls')),
    path("About_us/", include('About_Us.urls')),
    path("Publish/", include('Publish.urls')),
    path('',views.base),
    path("accounts/", include('django.contrib.auth.urls')),
    path('logout/',views.logout_view),
    path('signup/',views.Signup)


    # path('accounts/', include('django.contrib.auth.urls')),

    #     path(r"^logout/",views.logout_view)
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
