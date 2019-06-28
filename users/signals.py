from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from store.models import Post, Lesson, Subscriber


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
            Profile.objects.create(user=instance)
            Subscriber.objects.create(current_user = instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()    