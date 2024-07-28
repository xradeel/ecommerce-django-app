from django.shortcuts import render


def cart(request):
    return render(request, 'shop/shop-cart.html')

def checkout(request):
    return render(request, 'shop/shop-checkout.html')

def compare(request):
    return render(request, 'shop/shop-compare.html')

def filter(request):
    return render(request, 'shop/shop-filter.html')

def shopGrid(request):
    return render(request, 'shop/shop-grid.html')

def product(request):
    return render(request, 'shop/shop-product.html')

def wishlist(request):
    return render(request, 'shop/shop-wishlist.html')

