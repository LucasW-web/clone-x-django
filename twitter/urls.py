from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('follow/<int:user_id>/', views.follow_toggle_view, name='follow_toggle'),
    path('like/<int:tweet_id>/', views.like_toggle_view, name='like_toggle'),
    path('comment/<int:tweet_id>/', views.add_comment_view, name='add_comment'),
    path('profile/', views.profile_view, name='profile'), # Certifique-se de que esta linha existe!
]



