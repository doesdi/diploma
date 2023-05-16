from django.contrib import admin

from .models import *

admin.site.register(tasks)
admin.site.register(role)
admin.site.register(client)
admin.site.register(orders)
admin.site.register(inventory)
admin.site.register(sales)
admin.site.register(users)
admin.site.register(review)
admin.site.register(application)
