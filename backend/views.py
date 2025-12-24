from django.shortcuts import render
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration.html')

def vhod(request):
    return render(request, 'vhod.html')

def catalog(request):
    return render(request, 'catalog.html')

