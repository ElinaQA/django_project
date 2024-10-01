from django.urls import path
from app3.views import courses, lessons, chat

urlpatterns = [
    path('courses', courses),
    path('lessons', lessons),
    path('chat', chat),
]