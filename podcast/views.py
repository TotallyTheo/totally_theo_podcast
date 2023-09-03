from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


from .models import Episode

def home(request):
    latest_episodes = Episode.objects.order_by('-release_date')[:3]
    return render(request, 'home.html', {'latest_episodes': latest_episodes})

def episodes(request):
    all_episodes = Episode.objects.all()
    return render(request, 'episodes.html', {'all_episodes': all_episodes})

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    # Your dashboard view logic here (e.g., display user-specific content)
    return render(request, 'dashboard.html')
