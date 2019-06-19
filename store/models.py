from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator('0.01')])
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str___(self):
		return self.title