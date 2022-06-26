from re import U

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# Create your views here.
def authLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee.profile')
        else:
            messages.error(request, 'Your user name and password is wrong.')

    return render(request, 'login.html')


def forgot(request):
    return render(request, 'forgot.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get("fullName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        print(username)
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                user.save()
                messages.success(request, "Register successfully")
                return redirect('login')
        else:
            messages.error(request, "Password did not matched")

    return render(request, 'register.html')


def authLogOut(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')
