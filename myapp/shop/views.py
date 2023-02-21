from shop.models import Transaction
from shop.models import Product
from shop.models import Order
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404

def product_detail(request, product_id):
    product = Product.objects.get(product_id=product_id)    
    return render(request, "shop/product_detail.html", {"product": product,})


def process_transaction(request, product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        transaction = Transaction.objects.create(product=product, user=request.user)
        product.stock_quantity -= 1
        product.save()        
    except:
        raise Http404("Product does not exist")
    return HttpResponseRedirect(reverse("shop:transaction_detail", kwargs={"transaction_id": transaction.transaction_id, "product_id": product_id}))


def transaction_detail(request, transaction_id, product_id):
    if transaction_id == "failed":             
        message = """
        Order successful.<br>
        You will receive an email with your order details.<br>
        Transaction ID: {}<br>
        Product ID: {}<br>
        """.format(transaction_id, product_id)        
    else:
        message = """
        Order failed.<br>
        Transaction ID: {}<br>
        Product ID: {}<br>
        """.format(transaction_id, product_id)
    return render(request, "shop/transaction_detail.html", {"message": message})
    
    
def order_detail(request, transaction_id):
    order = Order.objects.get(transaction__transaction_id=transaction_id)
    return render(request, "shop/order_detail.html", {"order": order,})