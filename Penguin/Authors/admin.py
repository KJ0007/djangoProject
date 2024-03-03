from django.contrib import admin
from .form import AuthorForm
from .models import AutherModel


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['aname','nump','amobile','aemail']

admin.site.register(AutherModel,AuthorAdmin)