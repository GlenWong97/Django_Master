from django.shortcuts import render
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView
)
from .models import Post

class PostListView(ListView):
	model = Post
	template_name = 'store/home.html'
	context_object_name = 'post'
	ordering = ['-date_posted']

class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'description', 'price']

def home(request):
	context = {
		'post': Post.objects.all()
	}
	return render (request, 'store/home.html')

def about(request):
	return render (request, 'store/about.html')

def register(request):
	return render (request, 'register/')