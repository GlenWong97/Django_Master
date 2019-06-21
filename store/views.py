from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import FileSystemStorage
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Post

def home(request):
	context = {
		'post': Post.objects.all()
	}
	return render (request, 'store/home.html', context)

def upload(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		url = fs.url(name)
		print(uploaded_file.name)
		print(uploaded_file.size)
	return render(request, 'store/upload.html')

class PostListView(ListView):
	model = Post
	template_name = 'store/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'post'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'description', 'price']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'description', 'price']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post	
	success_url = "/"
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render (request, 'store/about.html')

def register(request):
	return render (request, 'register/')