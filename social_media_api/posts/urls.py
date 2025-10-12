from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# your existing router registrations

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.feed_view, name='feed'),
]