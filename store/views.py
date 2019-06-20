from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView
)
from .models import Post

def home(request):
	context = {
		'post': Post.objects.all()
	}
	return render (request, 'store/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'store/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'post'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	
class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'description', 'price', 'date_posted']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

def about(request):
	return render (request, 'store/about.html')

def register(request):
	return render (request, 'register/')