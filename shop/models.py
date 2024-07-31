from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name= models.CharField(max_length=250)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.TextField(max_length=500)
    long_description = models.TextField()
    size = models.CharField(max_length=255)
    availability =models.BooleanField(default=True)
    featured =models.BooleanField(default=False)
    popular =models.BooleanField(default=False)
    status =models.BooleanField(default=True)
    thumbnail1 = models.ImageField(upload_to='thumbnails/')
    thumbnail2 = models.ImageField(upload_to='thumbnails/')
    accesstoken = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)


class Product_images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to ='product-images/')

    
class OfferBanner(models.Model):
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='offer-banner/')
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

class OfferBanner(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='offer-banner/')
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    
