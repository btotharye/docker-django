from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Snake
from .forms import SnakeForm, SignUpForm
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'snakeapp/home.html', {})

@login_required
def dashboard(request):
    return render(request, 'snakeapp/dashboard.html', {})

@login_required
def mySnakes(request):
    if request.user.is_authenticated:
        snakes = Snake.objects.filter(owner=request.user)
        print(snakes)
        print(request.user)
        return render(request, 'snakeapp/mysnakes.html', {'snakes': snakes})
    else:
        return render(request, 'snakeapp/mysnakes.html', {'snakes': ''})


def snake_detail(request, pk):
    snake = get_object_or_404(Snake, pk=pk)
    return render(request, 'snakeapp/snake_detail.html', {'snake': snake})

@login_required
def snake_add(request):
    if request.method == "POST":
        form = SnakeForm(request.POST)
        if form.is_valid():
            snake = form.save(commit=False)
            snake.owner = request.user
            snake.date_added = timezone.now()
            snake.save()
            return redirect('snake_detail', pk=snake.pk)
    else:
        form = SnakeForm()
    return render(request, 'snakeapp/snake_edit.html', {'form': form})

@login_required
def snake_edit(request, pk):
    snake = get_object_or_404(Snake, pk=pk)
    if request.method == "POST":
        form = SnakeForm(request.POST, instance=snake)
        if form.is_valid():
            snake = form.save(commit=False)
            snake.owner = request.user
            snake.date_added = timezone.now()
            snake.save()
            return redirect('snake_detail', pk=snake.pk)
    else:
        form = SnakeForm(instance=snake)
    return render(request, 'snakeapp/snake_edit.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
