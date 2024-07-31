from django.db import models

# Create your models here.


class Banner_feature(models.Model):
    #title, icon, status, upadetat
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    icon = models.ImageField(upload_to='banner-feature/')
    updatedat = models.DateTimeField(auto_now=True)