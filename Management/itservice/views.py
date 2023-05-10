from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import *
from .models import *


def Main(request):
    return render(request, 'itservice/main.html')


def Profile(request):
    user = users.objects.all()
    return render(request, 'itservice/profile.html', {'user': user})


def Clients(request):
    if request.method == 'POST':
        form_client = AddClientFrom(request.POST)
        if form_client.is_valid():
            form_client.save()
            return redirect('clients')
    else:
        form_client = AddClientFrom()
    clients = client.objects.all()
    return render(request, 'itservice/clients.html', {'clients': clients, 'form': form_client})


def Inventory(request):
    if request.method == 'POST':
        form_invent = AddInventFrom(request.POST)
        if form_invent.is_valid():
            form_invent.save()
            return redirect('inventory')
    else:
        form_invent = AddInventFrom()
    invent = inventory.objects.all()
    return render(request, 'itservice/inventory.html', {'invent': invent, 'form': form_invent})


def Orders(request):
    if request.method == 'POST':
        form_order = AddOrdersFrom(request.POST)
        if form_order.is_valid():
            form_order.save()
            return redirect('orders')
    else:
        form_order = AddOrdersFrom()
    order = orders.objects.all()
    return render(request, 'itservice/orders.html', {'order': order, 'form': form_order})


def Sales(request):
    if request.method == 'POST':
        form_sales = AddSalesFrom(request.POST)
        if form_sales.is_valid():
            form_sales.save()
            return redirect('sales')
    else:
        form_sales = AddSalesFrom()
    sale = sales.objects.all()
    return render(request, 'itservice/sales.html', {'sale': sale, 'form': form_sales})


def Tasks(request):
    if request.method == 'POST':
        form = AddTaskFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = AddTaskFrom()
    task = tasks.objects.all()
    return render(request, 'itservice/tasks.html', {'task': task, 'form': form})
