from django.shortcuts import render

# Create your views here.
def info(r):
    return render(r,"About_Us/about_us.html")