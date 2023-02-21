from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
import uuid


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    stock_quantity = models.PositiveIntegerField(default=10)

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"product_id": self.product_id})

class Transaction(models.Model): 
    transaction_id = models.UUIDField(primary_key=True, editable=False, blank=False, default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, editable=False, blank=False, default=uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("shop:order_detail", kwargs={"transaction_id": self.transaction.transaction_id})
    
    def get_full_url(self):
        return "{}{}".format(settings.FULL_SITE_URL, self.get_absolute_url())


@receiver(post_save, sender=Transaction)
def create_order(sender, instance, created, **kwargs):
    if created:
        order = Order.objects.create(transaction=instance, product=instance.product, user=instance.user)
        sender = "admin@reservation.com"
        receiver = instance.user.email
        subject = "Order confirmation"
        message = f"Order for product {instance.product.name} has been confirmed. Your can view your order at {order.get_full_url()}"
        send_mail(subject, message, sender, [receiver], fail_silently=False)