from django.urls import path
from . import views

urlpatterns = [
    # your existing paths here (register, login, etc.)
    path('follow/<int:user_id>/', views.follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow-user'),
]