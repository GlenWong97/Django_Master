from django import forms 
from .models import Lesson, Feedback, Quiz, Question, Result

class LessonForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = ('title', 'file')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('rating', 'comment')

class Ans_sheet(forms.ModelForm):
	class Meta:
		model = Result
		fields = ('q1','q2','q3','q4','q5','q6','q7','q8','q9','q10')

class QuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		fields = ('title',)