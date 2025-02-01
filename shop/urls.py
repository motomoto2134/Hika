from django.urls import path
from .views import *

urlpatterns = [
    path('', catalog, name='catalog'),
    path('product_detail/<int:product_id>/',product_detail, name="product"),
    path('create_order/<int:product_id>/',create_order, name="create_order"),
    path('orders/',orders, name="orders")
]