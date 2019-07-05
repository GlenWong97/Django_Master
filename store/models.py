from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from dynamic_models.models import AbstractModelSchema, AbstractFieldSchema

class ModelSchema(AbstractModelSchema):
    pass

class FieldSchema(AbstractFieldSchema):
    pass

class Feedback(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.CharField(max_length = 100, blank=True)
	rating = models.DecimalField(default=-1, decimal_places=2, max_digits=3)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.user) + " : " + str(self.comment) + " - " + str(self.rating)

	def get_absolute_url(self):
		return reverse('comment_upload', kwargs={'pk' : self.pk})
	
	def save(self, *args, **kwargs):
         super(Feedback, self).save(*args, **kwargs)

class Post(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(default = 'default0.jpg', upload_to='course_image/')
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=6)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	feedback = models.ManyToManyField(Feedback)
	n_rating = models.IntegerField(default=0)
	n_subs = models.IntegerField(default=0)
	
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

	@property
	def lessons(self):
		return self.lesson_set.all()

class Quiz(models.Model):
	title = models.CharField(max_length=30)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
	time = models.IntegerField()
	t_score = models.IntegerField()

	def __str__(self):
		return self.title
	
	@property
	def questions(self):
		return self.question_set.all()

	@property
	def results(self):
		return self.result_set.all()

class Result(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=False, blank=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
	score = models.IntegerField()

	def __str__(self):
		return str(self.quiz) + ": " + str(self.user)

class Question(models.Model):
	title = models.CharField(max_length=30)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=False, blank=False)	
	choices = models.CharField(max_length=50)
	time = models.IntegerField()
	answer = models.CharField(max_length=50)
	user_answer = models.CharField(max_length=40)

	def __str__(self):
		return self.title

class Lesson(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(upload_to="lesson/pdf")
	date_posted = models.DateTimeField(default=timezone.now)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('lesson_upload', kwargs={'pk': self.pk})

	# def delete(self, *args, **kwargs):
	# 	self.file.delete()
	# 	self.title.delete()
	# 	super().delete(*args, **kwargs)
		
class Subscriber(models.Model):
	users = models.ManyToManyField(Post)
	current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.current_user.username

	@classmethod
	def subscribe(cls, current_user, new_sub):
		sub, created = cls.objects.get_or_create(
			current_user=current_user
		)
		sub.users.add(new_sub)

	@classmethod
	def unsubscribe(cls, current_user, new_sub):
		sub, created = cls.objects.get_or_create(
			current_user=current_user
		)
		sub.users.remove(new_sub)