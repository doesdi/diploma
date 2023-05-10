from datetime import date, datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class role(models.Model):
    role_name = models.CharField(max_length=50, verbose_name="Название роли")

    def __str__(self):
        return self.role_name


class users(AbstractUser):
    user_phone = models.CharField(max_length=40, verbose_name="Номер телефона")
    user_note = models.CharField(max_length=50, verbose_name="Примечание")
    user_time = models.DateField(default=date.today, verbose_name="Дата начала работы")
    user_photo = models.ImageField(upload_to="photos/%y/%m/%d/", verbose_name="Фото сотрудника")


class tasks(models.Model):
    task_name = models.CharField(max_length=50, verbose_name="Название задачи")
    task_description = models.CharField(max_length=1000, verbose_name="Описание задачи")
    task_time = models.DateTimeField(default=datetime.now, verbose_name="Крайний срок")
    task_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return self.task_name


class client(models.Model):
    Type = (
        ('Компания', 'Компания'),
        ('Физ.Лицо', 'Физ.Лицо')
    )

    Found = (
        ('Знакомые', 'Знакомые'),
        ('Интернет', 'Интернет'),
        ('Реклама', 'Реклама')
    )

    client_type = models.CharField(max_length=15, choices=Type,
                                   default='Физ.лицо', verbose_name="Тип клиента")
    client_name = models.CharField(max_length=50, verbose_name="Имя клиента")
    client_phone = models.CharField(max_length=40, verbose_name="Номер телефона")
    client_email = models.CharField(max_length=100, verbose_name="Email")
    client_address = models.CharField(max_length=50, verbose_name="Адрес")
    client_found = models.CharField(max_length=15, choices=Found, default='Знакомые',
                                    verbose_name="Откуда клиент узнал о нас?")

    def __str__(self):
        return self.client_name


class orders(models.Model):
    order_name = models.CharField(max_length=50, verbose_name="Название заказа")
    order_description = models.CharField(max_length=1000, verbose_name="Требования к заказу")
    order_time = models.DateTimeField(default=datetime.now, verbose_name="Крайний срок")
    order_price = models.IntegerField(verbose_name="Ориентировочная стоимость")
    order_client = models.ForeignKey(client, on_delete=models.PROTECT, verbose_name="Клиент")
    order_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return self.order_name


class inventory(models.Model):
    Type = (
        ('Устройство', 'Устройство'),
        ('Запчасти', 'Запчасти')
    )
    inventory_type = models.CharField(max_length=15, choices=Type,
                                      default='Устройство', verbose_name="Категория")
    inventory_article = models.IntegerField(verbose_name="Артикул")
    inventory_name = models.CharField(max_length=50, verbose_name="Название")
    inventory_color = models.CharField(max_length=40, verbose_name="Цвет")
    inventory_condition = models.CharField(max_length=100, verbose_name="Состояние")
    inventory_description = models.CharField(max_length=1000, verbose_name="Описание")
    inventory_client = models.ForeignKey(client, on_delete=models.PROTECT, null=True, verbose_name="Клиент")

    def __str__(self):
        return self.inventory_name


class sales(models.Model):
    sales_name = models.CharField(max_length=100, verbose_name="Наименование работы")
    sales_comment = models.CharField(max_length=100, verbose_name="Комментарий")
    sales_price = models.CharField(max_length=100, verbose_name="Цена")
    sales_time = models.DateTimeField(default=datetime.today, verbose_name="Время продажи")
    sales_client = models.ForeignKey(client, on_delete=models.PROTECT)

    def __str__(self):
        return self.sales_name
