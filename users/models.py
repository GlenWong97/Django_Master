from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'profile_pics/default.jpg', upload_to='profile_pics')
    gender = models.CharField(
        max_length = 12,
        choices = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),
            ('Justin Lu', 'Justin Lu')
        ],
        default = 'Justin Lu'
    )
    bio = models.CharField(max_length = 1000, blank = True, default = '-')
    def __str__(self):
        return f'{self.user.username} Profile'