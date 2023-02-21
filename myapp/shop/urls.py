from django.urls import path
from shop.views import product_detail
from shop.views import transaction_detail
from shop.views import order_detail
from shop.views import process_transaction

app_name = "shop"

urlpatterns = [
    path("product/<uuid:product_id>/", product_detail, name="product_detail"),
    path("process_transaction/<uuid:product_id>/", process_transaction, name="process_transaction"),
    path("transaction/<uuid:product_id>/<uuid:transaction_id>/", transaction_detail, name="transaction_detail"),
    path("order/<uuid:transaction_id>/", order_detail, name="order_detail"),
]