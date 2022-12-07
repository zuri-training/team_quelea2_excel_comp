from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import * 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

@login_required(login_url="login_page")
def dashboard_page(request):
    return render(request, 'pages/dashboard.html')

@login_required(login_url="login_page")
def profile_page(request):
    return render(request, 'pages/profile.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard_page')
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f'accouunt created for {user.username} succefully')
            return redirect('login_page')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'pages/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard_page')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f'{user.username} logged in successfully')
            if 'next' in request.GET:
                return redirect(request.GET.get('next'))
            else:
                return redirect('dashboard_page')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'pages/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login_page')


# sending 404 page in django
