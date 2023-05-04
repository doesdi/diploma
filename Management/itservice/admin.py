from django.contrib import admin

from .models import *

admin.site.register(tasks)
admin.site.register(role)
admin.site.register(client)
admin.site.register(orders)
admin.site.register(inventory)
admin.site.register(sales)
