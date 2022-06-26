from multiprocessing.connection import Client

from django.shortcuts import render

from .models import About, Client, Slider


def home(request):
    about = About.objects.all()[0]
    slider = Slider.objects.all()
    clients = Client.objects.all()
    return render(request, 'index.html', {'about': about, "slider": slider, "clients": clients})


