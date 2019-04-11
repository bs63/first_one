from django.contrib import admin

from .models import Client, Table, Waiter
from .models import Dishes, Order, Menu, Review


admin.site.register(Client)
admin.site.register(Table)
admin.site.register(Waiter)
admin.site.register(Dishes)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Review)
