from django.shortcuts import render
from .models import AutherModel
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def AuthorList(r):
    obj=AutherModel.objects.all()
    return render(r,"Authors/author.html",context={'obj':obj})
