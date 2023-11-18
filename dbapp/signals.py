# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User) # fara asta nu merg user profiles (decat daca le creez manual)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User) # fara asta nu merg user profiles (decat daca le creez manual)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
