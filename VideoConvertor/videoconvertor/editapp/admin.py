import imp
from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProf(admin.ModelAdmin):
    list_display = ('user','DateOfBirth','status')
    list_filter = ['DateOfBirth']

admin.site.register(UserProfile,UserProf)