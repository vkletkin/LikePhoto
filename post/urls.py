from django.urls import path
from .views import task, show_orders, show_products

urlpatterns = [
    path("task/", task, name="task"),
    path("show_orders/", show_orders, name="show_orders"),
    path("show_products/", show_products, name="show_products"),
]
