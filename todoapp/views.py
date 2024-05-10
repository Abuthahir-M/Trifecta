from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        priority = request.POST.get('priority')
        new_todo = Todo(user=request.user, todo_name=task_name, priority=priority)
        new_todo.save()

    in_progress_count = Todo.objects.filter(user=request.user, status=False).count()

    all_todos = Todo.objects.filter(user=request.user)

    search_query = request.GET.get('search')
    if search_query:
        all_todos = all_todos.filter(todo_name__icontains=search_query)

    context = {
        'todos': all_todos,
        'in_progress_count': in_progress_count
    }
        
    return render(request, 'todoapp/index.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 8:
            messages.error(request, 'Password must be atleast 8 characters')
            return redirect('register')
        
        get_allUsers_by_username = User.objects.filter(username=username)
        if get_allUsers_by_username:
            messages.error(request, 'Username already exist, try another.')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, 'User successfully created, LOGIN now')
        return redirect('login-page')

    return render(request, 'todoapp/register.html')

def logoutUser(request):
    logout(request)
    return redirect('login-page')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('pass_word')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request, 'please check username & password or User does not exist')
            return redirect('login-page')

    return render(request, 'todoapp/login.html')

@login_required
def deleteTask(request, name):
    delete_todo = Todo.objects.filter(user=request.user, todo_name=name)
    delete_todo.delete()
    return redirect('home-page')

@login_required
def updateStatus(request, name):
    get_todo = Todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('home-page')