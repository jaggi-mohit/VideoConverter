from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):

    if created:
        UserProfile.objects.create(user=instance)
        print("Profile Created*********")

#post_save.connect(create_profile,sender=User)

@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):

    if created==False:
        instance.userprofile.save()
        print("profile updated.............")
