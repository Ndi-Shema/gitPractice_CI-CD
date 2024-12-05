from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

# View for listing tasks (accessible only to logged-in users)
@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user).order_by('-id')  # Fetch user's tasks
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# View for adding tasks (accessible only to logged-in users)
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category', '')
        Task.objects.create(title=title, category=category, owner=request.user)
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

# View for updating task completion status (accessible only to logged-in users)
@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id, owner=request.user)
    if request.method == 'POST':
        task.completed = not task.completed  # Toggle the completion status
        task.save()
        return JsonResponse({'status': 'success', 'completed': task.completed})
    return JsonResponse({'status': 'failed'})

# View for user signup
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful! You can now log in.")
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'todo/signup.html', {'form': form})

# Use Django's built-in LoginView to handle login
class CustomLoginView(LoginView):
    template_name = 'todo/login.html'  # Optional: If you have a custom login template

# Home view (only accessible to logged-in users)
@login_required
def home(request):
    return render(request, 'todo/home.html')

# List all tasks for the logged-in user
@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

# Add a new task
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user  # Set the logged-in user as the owner
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

# Update task completion status
@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        return redirect('task_list')  # Prevent other users from updating someone else's task
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
