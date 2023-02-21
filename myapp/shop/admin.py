from django.contrib import admin
from shop.models import Product
from shop.models import Order
from shop.models import Transaction

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Transaction)