from django.shortcuts import render
from .models import Product

# Create your views here.
# views.py
def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products':products})