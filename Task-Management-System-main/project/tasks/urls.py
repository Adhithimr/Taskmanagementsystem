from django.urls import path
from .views import TaskListCreateView, TaskDetailView, login_page, home
from . import views
urlpatterns = [
    path('', home, name='welcome'),
    path('tasks/', TaskListCreateView.as_view(), name='Task-List'),
    path('tasks/<int:task_id>/', TaskDetailView.as_view(), name='task-detail'),
    path('register/', views.register_user, name='register'),
    path('login/', login_page, name='login_page'),
    
]