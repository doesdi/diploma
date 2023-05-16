"""
URL configuration for Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from Management import settings
from itservice import views
from itservice.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', Logout_user, name="logout"),
    path('profile/', views.Profile, name="profile"),
    path('profile-edit/', ProfileUpdateView.as_view(), name="profile-edit"),
    path('clients/', views.Clients, name="clients"),
    path('sales/', views.Sales, name="sales"),
    path('orders/', views.Orders, name="orders"),
    path('orders-change/', views.Change_Order_st, name="orders-change"),
    path('inventory/', views.Inventory, name="inventory"),
    path('tasks/', views.Tasks, name="tasks"),
    path('tasks-change/', views.Change_Task_st, name="tasks-change"),
    path('applications/', views.Аpplications, name="applications"),
    path('staff/', views.st, name="staff"),
    path('staff-add/', views.Staff, name="staff-add"),
    path('applications-add/', views.Application, name="applications_add"),
    path('applications-change/', views.Change_appl_status, name="applications-change"),
    path('home/', views.Home, name="home"),
    path('review/', views.Rev, name="review"),
    path('review-add/', views.Review, name="review_add"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound