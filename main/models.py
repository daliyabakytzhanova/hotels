from django.db import models


# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250, default="")
    host = models.CharField(max_length=250, default="")
    rank = models.IntegerField(default=0)
    price = models.CharField(max_length=250, default=0)
    background = models.ImageField(upload_to="hotels", null=True, blank =True)

    def __str__(self):
        return self.name


class Zakaz(models.Model):
    name = models.CharField(max_length=250, default="")
    surname = models.CharField(max_length=250, default="")
    passport = models.IntegerField(default=0)
    hotel = models.CharField(max_length=250, default="")
    telephone = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.username
