from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=15)
    subject = models.CharField(max_length=250)
    accesstoken = models.CharField(max_length=250)
    message = models.TextField()
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
