from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
	TemplateView
)
from .models import Post, Lesson
from .forms import LessonForm
from django.urls import reverse, reverse_lazy

def home(request):
	queryset__list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(title__icontains=query)
	context = {
		
		'queryset_list': queryset_list
	}
	return render (request, 'store/home.html', context)

def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		context['url'] = fs.url(name)
	return render(request, 'store/upload.html', context)


def delete_lesson(request, pk):
	if request.method == 'POST':
		lesson = Lesson.objects.get(post__pk=post__pk)
		lesson.delete()
	return redirect('/')

# def upload_lesson(request):
# 	if request.method == 'POST':
# 		form = LessonForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('')
# 		else:
# 			form = LessonForm()
# 		return render(request, 'upload_lesson.html', {'form' : form})

class LessonListView(ListView):
	model = Lesson
	template_name = 'store/uploaded_lesson.html'
	context_object_name = 'lesson'	
		
	def get_queryset(self):
		return Lesson.objects.filter(post_id=self.kwargs.get('post_id'))

class UploadLessonView(CreateView):
	model = Lesson
	fields = ['title', 'file']	
	template_name = 'store/upload_lesson.html'
	success_url = '../'

	def form_valid(self, form):
		form.instance.post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
		return super(UploadLessonView, self).form_valid(form)



class PostListView(ListView):
	model = Post
	template_name = 'store/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'post'
	ordering = ['-date_posted']
	paginate_by = 8

class UserPostListView(ListView):
	model = Post
	template_name = 'store/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'post'
	paginate_by = 8

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

	
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'image', 'description', 'price']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'image', 'description', 'price']

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