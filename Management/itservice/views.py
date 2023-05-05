from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def Main(request):
    return render(request, 'itservice/main.html')


def Profile(request):
    return render(request, 'itservice/profile.html')


def Clients(request):
    return render(request, 'itservice/clients.html')


def Inventory(request):
    return render(request, 'itservice/inventory.html')


def Orders(request):
    return render(request, 'itservice/orders.html')


def Sales(request):
    return render(request, 'itservice/sales.html')


def Tasks(request):

    task = tasks.objects.all()
    return render(request, 'itservice/tasks.html', {'task': task})



