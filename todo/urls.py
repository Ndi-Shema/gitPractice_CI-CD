from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView  # Import LoginView and LogoutView
from . import views

urlpatterns = [
    # Login and Signup URLs
    path('login/', LoginView.as_view(), name='login'),  # Use the built-in LoginView for login
    path('signup/', views.signup, name='signup'),  # Custom signup view

    # Task-related URLs
    path('tasks/', views.task_list, name='task_list'),  # List tasks
    path('tasks/add/', views.add_task, name='add_task'),  # Add a new task
    path('tasks/update/<int:task_id>/', views.update_task, name='update_task'),  # Update a task's status

    # Logout URL
    path('logout/', LogoutView.as_view(), name='logout'),  # Use built-in LogoutView for logout
]
