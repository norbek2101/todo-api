from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('todo/', TaskListView.as_view()),
    path('todo/<int:pk>/', TaskDetailView.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)