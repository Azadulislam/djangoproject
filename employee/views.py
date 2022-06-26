from django.http import HttpResponse
from django.shortcuts import render


def employee(request):
    return render(request, 'employee/employee.html')


def profile(request):
    return render(request, 'employee/profile.html')
