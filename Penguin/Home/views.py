from django.shortcuts import render,redirect
from .form import SignupForm

# Create your views here.
def base(r):
    return render(r,"base.html")


def logout_view(r):
    return render(r,"registration/logout.html")


def Signup(r):
    form=SignupForm()
    if r.method=='POST':
        form=SignupForm(r.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login/')
    return render(r,"registration/login.html",context={"form":form})


