from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def index(request):
    username = request.user.username
    if request.method == "POST":
        room_name = request.POST.get('room_name')
        return redirect('chat_room', room_name=room_name)
    return render(request, 'index.html', { 'username' : username })

@login_required(login_url='login')
def chat_room(request, room_name):
    username = request.user.username
    return render(request, 'chat_room.html', {'room_name': room_name, 'username': username})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')