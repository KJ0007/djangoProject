from django.shortcuts import render,redirect
from .form import PublisherForm
from .models import PublisherModel

def push(r):
    form=PublisherForm()
    if r.method=='POST':
        form=PublisherForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PublisherForm()

    return render(r,"Publish/publish.html",context={'form':form})
#
# HTTPRespose("<h1>sdf</h1>")
# render(r,templter,cointext)
# redirect(base)

