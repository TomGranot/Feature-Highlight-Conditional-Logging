from celery.decorators import task
from shop.models import Product
import time
import random

@task(name="myapp.tasks.fill_stock")
def fill_stock():
    products = Product.objects.all()
    for product in products:        
        # A long running task that fetches data from an external API to fill the stock        
        # action 1
        # action 2
        # ...
        # action n        
        stock = random.randint(0, 250)
        if stock != 0:
            product.stock_quantity = stock
            product.save()
        else:
            product.delete()