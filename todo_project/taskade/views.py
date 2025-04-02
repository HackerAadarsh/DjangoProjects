from django.shortcuts import render, get_object_or_404, redirect
from .models import TODOO
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

# User Signup
def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('task_list')
    return render(request, 'auth/signup.html')

# User Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('task_list')
    return render(request, 'auth/loginn.html')

# User Logout
def logout_user(request):
    logout(request)
    return redirect('login')  # ✅ Fixed redirect

# Task List (Only for Logged-in Users)
@login_required
def task_list(request):
    tasks = TODOO.objects.filter(user=request.user)  # ✅ Show only the logged-in user's tasks
    return render(request, 'tasks/todo.html', {'tasks': tasks})

# Add Task
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('task_title', '')  # ✅ Prevent KeyError
        description = request.POST.get('task_description', '')  # ✅ Include description
        TODOO.objects.create(title=title, description=description, user=request.user)  # ✅ Fixed
    return redirect('task_list')

# Update Task
@login_required
def update_task(request, task_id):
    task = TODOO.objects.get(id=task_id, user=request.user)
    task.completed = not task.completed  # ✅ Now `completed` exists in `models.py`
    task.save()
    return redirect('task_list')


def edit_task(request, id):
    task = get_object_or_404(TODOO, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list after editing
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

# Delete Task
@login_required
def delete_task(request, task_id):
    task = TODOO.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')
