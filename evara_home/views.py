from django.shortcuts import render
from shop.models import Product

def home(request):
    products = Product.objects.all()
    for product in products:
        product.discounted_price = round(product.price - (product.price * (product.discount / 100)),2)
    return render(request, 'evara_home/index.html', {'products':products})