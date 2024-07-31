from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField( max_length=250)
    author = models.CharField( max_length=250)
    content = models.TextField()
    published = models.BooleanField(default=True)
    accesstoken = models.CharField( max_length=250)
    tags = models.CharField( max_length=250)
    summary = models.CharField( max_length=250)
    read_time = models.IntegerField()
    image = models.ImageField(upload_to='blogs/')
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)