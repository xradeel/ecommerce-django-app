from django.db import models

# Create your models here.

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team-member/')
    designation= models.CharField(max_length=255)
    facebook= models.CharField(max_length=255, default='#')
    insta= models.CharField(max_length=255, default='#')
    twitter= models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)


class Persona(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='personas/')
    organization= models.CharField(max_length=255)
    message = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

class MainBranches(models.Model):
    image = models.ImageField(upload_to='team-member/')
    address= models.CharField(max_length=255)
    street= models.CharField(max_length=255)
    postalcode= models.CharField(max_length=255, default='NY 00000, USA')
    status = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)