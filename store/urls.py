from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='store-home'),
    path('about/', views.about, name='store-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),   
    path('post/new/', PostCreateView.as_view(), name='post-create'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
