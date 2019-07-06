from django.urls import path
from django.conf.urls import url
from users import views as user_views
from chat import views as chat_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
    LessonListView,
    UploadLessonView,
    UserPostListView,
    LessonDeleteView,
    SubListView,
    change_sub,
    InteractiveListView,
    QuestionListView
)
from . import views

urlpatterns = [    
    # path('sub_home', SubListView.as_view(), name='store-sub_home'),
    path('', SubListView.as_view(), name='store-home'),
    path('search/', PostListView.as_view(), name='store-search'),
    path('chat/', chat_views.index, name='chat'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='store-about'),    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:post_id>/comment_upload/', UploadCommentView.as_view(), name='comment_upload'),    
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:post_id>/lesson_upload/', UploadLessonView.as_view(), name='lesson_upload'),   
    path('post/<int:post_id>/interactive/', InteractiveListView.as_view(), name='interactive'),
    path('post/<int:post_id>/interactive/<int:quiz_id>/', QuestionListView.as_view(), name='quiz'),      
    path('post/<int:post_id>/lesson_uploaded/', LessonListView.as_view(), name='lesson_uploaded'),    
    path('post/lesson_uploaded/<int:pk>/', LessonDeleteView.as_view(), name='lesson_delete'),
    path('lesson_uploaded/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/change_sub/<slug:operation>/', views.change_sub, name='change_sub'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),   
    path('password-reset/',
     auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),   
    path('password-reset/done/',
     auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),   
    path('password-reset/confirmed/<uidb64>/<token>',
     auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),   
    path('password-reset-complete/',
     auth_views.PasswordResetView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),   
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)