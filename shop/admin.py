from django.contrib import admin
from .models import Categories, Product_images, Product
# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_id', 'createdat')

admin.site.register(Categories, CategoriesAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'createdat')

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'photo')

admin.site.register(Product_images, ProductImageAdmin)