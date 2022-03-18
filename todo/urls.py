from django.urls import path
from todo.views import TaskListView, TaskDetailView

urlpatterns = [
    path('todo/', TaskListView.as_view()),
    path('todo/<int:pk>/', TaskDetailView.as_view()),
    
]
