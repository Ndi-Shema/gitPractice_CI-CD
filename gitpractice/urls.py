from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView  # Import LoginView
from todo import views  # Import views from your todo app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),  # Use Django's built-in LoginView for login
    path("signup/", views.signup, name="signup"),  # Your custom signup view
    path("tasks/", include("todo.urls")),  # Include task URLs (make sure todo/urls.py exists)
    path("", views.home, name="home"),  # Home page for logged-in users
]
