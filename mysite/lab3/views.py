from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from .forms import StatusForm
from .models import Status


def home(request):
    user_status = None

    if request.user.is_authenticated:
        user_status = Status.objects.filter(user=request.user).first()

    return render(request, 'lab3/home.html', {'user_status': user_status})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)  # User obj is created, but not is saved
            cd = user_form.cleaned_data
            new_user.set_password(cd['password'])  # setting chosen password
            new_user.save()  # saving User
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to='lab3:home')

                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'lab3/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to='lab3:home')

                else:
                    return HttpResponse("Disabled account")
        else:
            return HttpResponse("Invalid login")
    else:
        form = LoginForm
    return render(request, 'lab3/login.html', {'form': form})


def set_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            status.user = request.user
            status.save()
            return redirect(to='lab3:home')
    else:
        form = StatusForm()
    return render(request, 'lab3/set_status.html', {'form': form})
