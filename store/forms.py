from django import forms
from .models import Lesson, Feedback

class LessonForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = ('title', 'file')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('comment', 'rating')