from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.shopGrid, name='shop.main'),
    path('cart/', views.cart, name='shop.cart'),
    path('checkout/', views.checkout, name='shop.checkout'),
    path('compare/', views.compare, name='shop.compare'),
    path('product/', views.product, name='shop.product'),
    path('wishlist', views.wishlist, name='shop.wishlist'),
    path('filter', views.filter, name='shop.filter'),
]
