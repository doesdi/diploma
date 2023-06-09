from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView, CreateView
from django.core.mail import EmailMessage
import pandas as pd
import codecs
from django.http import FileResponse
from openpyxl.workbook import Workbook


from .forms import *
from .models import *

import json
from django.core.mail import send_mail


# import smtplib
# smtpObj = smtplib.SMTP('smtp.mail.ru', 465)
# smtpObj.starttls()
# smtpObj.login('itservicediplom1@mail.ru', 'mmdSrKEW3YUUu2YpgysL')


def Main(request):
    user = request.user
    return render(request, 'itservice/main.html', {'user': user})


def Home(request):
    return render(request, 'itservice/home.html')


def Review(request):
    if request.method == 'POST':
        form_review = AddReview(request.POST)
        if form_review.is_valid():
            form_review.save()
            return redirect('home')
    else:
        form_review = AddReview()
    reviews = review.objects.all()
    return render(request, 'itservice/review-add.html', {'reviews': reviews, 'form': form_review})


def Rev(request):
    reviews = review.objects.all()
    return render(request, 'itservice/review.html', {'reviews': reviews})


def Application(request):
    if request.method == 'POST':
        form_appl = AddApplication(request.POST)
        if form_appl.is_valid():
            form_appl.save()
            return redirect('home')
    else:
        form_appl = AddApplication()
    applications = application.objects.all()
    return render(request, 'itservice/application-add.html', {'applications': applications, 'form': form_appl})


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


def Change_Task_st(request):
    body = json.loads(request.body)
    task = tasks.objects.get(pk=body["task_id"])
    task.task_active = not task.task_active
    task.save()
    return HttpResponse("true")


def Change_appl_status(request):
    body = json.loads(request.body)
    applications = application.objects.get(pk=body["application_id"])
    applications.application_active = not applications.application_active
    applications.save()
    return HttpResponse("true")


def Change_Order_st(request):
    body = json.loads(request.body)
    order = orders.objects.get(pk=body["order_id"])
    order.order_active = not order.order_active
    order.save()
    return HttpResponse("true")


def Аpplications(request):
    appl = application.objects.all()
    return render(request, 'itservice/applications.html', {'appl': appl})


def st(request):
    us = users.objects.all()
    return render(request, 'itservice/staff.html', {'us': us})


def Staff(request):
    if request.method == 'POST':
        form_staff = RegStaff(request.POST)
        if form_staff.is_valid():
            form_staff.save()
            return redirect('staff')
    else:
        form_staff = RegStaff()
    user = request.user
    us = users.objects.all()
    return render(request, 'itservice/staff-add.html', {'user': user, 'us': us, 'form': form_staff})


class LoginUser(LoginView):
    form_class = Login
    template_name = 'itservice/login.html'

    def get_success_url(self):
        print(1)
        return reverse_lazy('profile')


def Logout_user(request):
    logout(request)
    return redirect('tasks')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def Download_table(request):
    sale = sales.objects.all()
    data = []
    columns = ['Наименование работы', 'Комментарий', 'Цена', 'Время продажи', 'Клиент']
    for i in sale:
        print(i)
        data.append([i.sales_name, i.sales_comment, i.sales_price, i.sales_time, i.sales_client])
    df = pd.DataFrame(data, columns=columns)
    df['Время продажи'] = df['Время продажи'].dt.tz_localize(None)
    df.to_excel('itservice/Exel/Sale.xlsx', index=False)
    file = open('itservice/Exel/Sale.xlsx', "rb")
    return FileResponse(file)



