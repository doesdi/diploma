from django.shortcuts import render, redirect
from django.http import HttpResponse


def main(request):
    return render(request, 'itservice/main.html')


def profile(request):
    return render(request, 'itservice/profile.html')


def clients(request):
    return render(request, 'itservice/clients.html')


def inventory(request):
    return render(request, 'itservice/inventory.html')


def orders(request):
    return render(request, 'itservice/orders.html')


def sales(request):
    return render(request, 'itservice/sales.html')


def tasks(request):
    return render(request, 'itservice/tasks.html')



