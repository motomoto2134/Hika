from django.shortcuts import render
from .models import *

# Create your views here.
# views.py
def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products':products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product':product})

def create_order(request, product_id):
    if request.method == 'POST':
        quantity = request.POST['quantity']
        email = request.POST['email']
        address = request.POST['address']
        credit = request.POST['credit']
        Order.objects.create(
            addrss = address,
            email = email,
            card = credit,
            count = quantity
        )
    return render(request, 'shop/create_order.html' )

def orders(request):
    order = Order.objects.all()
    return render(request, 'shop/orders.html', {'order':order})