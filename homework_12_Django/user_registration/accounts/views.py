from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserLogin


def home(request):
    return render(request, 'accounts/home.html')


def home_login(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'accounts/home_login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            return redirect('home_login')
    else:
        form = UserLogin()
    return render(request, 'accounts/login.html', {'form': form})
