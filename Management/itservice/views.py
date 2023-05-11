from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .forms import *
from .models import *


def Main(request):
    user = request.user
    return render(request, 'itservice/main.html', {'user': user})


def Profile(request):
    user = request.user
    if request.method == 'POST':
        form_prof = ProfileFrom(request.POST)
        if form_prof.is_valid():
            form_prof.save()
            return redirect('sales')
    else:
        form_prof = ProfileFrom()
    return render(request, 'itservice/profile.html', {'user': user, 'form': form_prof})


class ProfileUpdateView(UpdateView):
    """
    Представление для редактирования профиля
    """
    model = users
    form_class = ProfileUpdateForm
    template_name = 'itservice/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = ProfileFrom(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = ProfileFrom(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')


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
