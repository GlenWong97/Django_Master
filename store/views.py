from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
	TemplateView
)
from django.http import Http404, HttpResponseRedirect
from .models import Post, Lesson, Subscriber, Feedback
from .forms import LessonForm, CommentForm
from django.urls import reverse, reverse_lazy

def home(request):
	queryset__list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(title__icontains=query)
	context = {
		'post': Post.objects.all(), 'subs' : subs, 'users': users, 'lesson': Lesson.objects.all()
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


# def delete_lesson(request, pk):
# 	if request.method == 'POST':
# 		lesson = Lesson.objects.get(pk=pk)
# 		lesson.delete()
# 	return redirect('/')

class LessonListView(ListView):
	model = Lesson
	template_name = 'store/uploaded_lesson.html'
	context_object_name = 'Lesson'	
		
	def get_queryset(self):
		if 	(Post.objects.get(id=self.kwargs.get('post_id')) in ((Subscriber.objects.get(current_user = self.request.user))).users.all()) or Post.objects.get(id=self.kwargs.get('post_id')).author == self.request.user:
			return Lesson.objects.filter(post_id=self.kwargs.get('post_id'))
		else:
			raise Http404
class UploadLessonView(CreateView):
	model = Lesson
	fields = ['title', 'file']	
	template_name = 'store/upload_lesson.html'
	success_url = '../'

	def form_valid(self, form):
		form.instance.post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
		return super(UploadLessonView, self).form_valid(form)	

class LessonDeleteView(DeleteView):
	model = Lesson
	template_name = 'store/lesson_confirm_delete.html'	
	success_url = '/'
	
	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.file.delete()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)

class PostListView(ListView):
	model = Post
	template_name = 'store/search.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'searchpost'
	ordering = ['-date_posted']
	paginate_by = 12

	def get_queryset(self, *args, **kwargs):
		object_list = super(PostListView, self).get_queryset(*args, **kwargs)
		search = self.request.GET.get('q', None)
		if search:
			object_list = object_list.filter(title__icontains = search)		
		return object_list

		

class SubListView(ListView):
	model = Post
	template_name = 'store/sub_home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 4

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = Post.objects.all()
		if self.request.user.is_authenticated:
			context['users'] = User.objects.exclude(id=self.request.user.id)
			sub = Subscriber.objects.get(current_user=self.request.user)
			context['subs'] = sub.users.all()
			context['mine'] = Post.objects.filter(author=self.request.user.id)
		return context


class UserPostListView(ListView):
	model = Post
	template_name = 'store/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'post'
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

	def get_context_data(self, *args, **kwargs):
	 	context = super(PostDetailView, self).get_context_data(*args, **kwargs)
	 	context['sub'] = ((Subscriber.objects.get(current_user = self.request.user))).users.all()
	 	context['form'] = CommentForm()
	 	return context

	def post(self, request, pk):
		post_x = Post.objects.get(pk=pk)
		form = CommentForm(request.POST)
		if form.is_valid():
			try:
				post_x.feedback.get(user = request.user).delete()
			except Feedback.DoesNotExist:
				None
			feedback = form.save(commit = False)
			feedback.user = request.user
			if len(feedback.comment) or feedback.rating != -1:
				feedback.save()
				get_object_or_404(Post, pk=pk).feedback.add(feedback)
			comment = form.cleaned_data['comment']
			rating = form.cleaned_data['rating']
			form = CommentForm()
			r = 0
			n = 0
			for i in list(post_x.feedback.all()):
				if i.rating <= 5 and i.rating >=1:
					n += 1
					r += i.rating
			if n == 0:
				post_x.n_rating = 0
			else:
				post_x.n_rating = 100 * r / n
			post_x.save()
		return HttpResponseRedirect(self.request.path_info)

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

def change_sub(request, operation, pk):
	new_sub = Post.objects.get(pk=pk)
	if operation == 'add':
		Subscriber.subscribe(request.user, new_sub)
		new_sub.n_subs += 1
		new_sub.save()
		return redirect('../../')
	elif operation == 'remove':
		Subscriber.unsubscribe(request.user, new_sub)
		new_sub.n_subs -= 1
		new_sub.save()
		return redirect('store-home')