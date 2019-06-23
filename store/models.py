from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class Post(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(default = 'default0.jpg', upload_to='course_image/')
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=6)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	rating = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk' : self.pk})

	def save(self, *args, **kwargs):
         super(Post, self).save(*args, **kwargs)
         img = Image.open(self.image.path)
         if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Lesson(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(upload_to="lesson/pdf")
	date_posted = models.DateTimeField(default=timezone.now)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, default=None)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('lesson_upload', kwargs={'pk': self.pk})