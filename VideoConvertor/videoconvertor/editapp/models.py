from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,default="")
    img=models.ImageField(upload_to="profile")
    DateOfBirth=models.DateField(null=True)
    PhoneNumber=models.CharField(max_length=10)
    Location=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    Cdate=models.DateTimeField(auto_now_add=True,null=True)
    Udate=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username
#signals*************
