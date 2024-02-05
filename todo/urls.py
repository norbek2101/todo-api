from django.urls import path
from todo.views import TaskListView, TaskDetailView, TasksbyUser

urlpatterns = [
    path('todo/', TaskListView.as_view()),
    path('todo/<int:pk>/', TaskDetailView.as_view()),
     path('tasksByUser/<int:id>/', TasksbyUser.as_view(), name='task-user'),
    
]
