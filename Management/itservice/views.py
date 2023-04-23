from django.shortcuts import render, redirect
from django.http import HttpResponse


def main(request):
    return render(request, 'itservice/main.html')
