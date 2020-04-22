from django.contrib import admin
from .models import Product, OrderItem, Order
from accounts.models import Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)