from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
    sittayma = models.BooleanField(default= True)
    video = models.URLField(max_length=500)
    lat = models.FloatField()
    longi = models.FloatField()
class passhash(models.Model):
    salt = models.CharField(max_length=200)
    user = models.CharField(max_length=200)

class contact(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    subject = models.TextField()
    email = models.EmailField()
    message = models.TextField()
class subscribe(models.Model):
    email = models.EmailField()
class bookings(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    plocation = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    min = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)


class comments(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.URLField(null=True, blank=True)

class user_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14,null=True,blank=True)
    company = models.CharField(max_length=200,null=True,blank=True)
    website = models.URLField(max_length=200,null=True,blank=True)
    street = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=80,null=True,blank=True)
    state = models.CharField(max_length=20,null=True,blank=True)
    pp = models.ImageField(upload_to='pics', null=True, blank=True)
    pd = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.user.first_name



class trecking(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics',null=True,blank=True)
    small_desc = models.TextField(null=True,blank=True)
    big_desc = models.TextField(null=True,blank=True)  
    price = models.IntegerField(null=True,blank=True)
    offer = models.BooleanField(default = False)
    sittayma = models.BooleanField(default= True)
    video = models.URLField(max_length=500,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    longi = models.FloatField(null=True,blank=True)

    def __self__(self):
        return self.name

class religious(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics',null=True,blank=True)
    small_desc = models.TextField(null=True,blank=True)
    big_desc = models.TextField(null=True,blank=True)  
    price = models.IntegerField(null=True,blank=True)
    offer = models.BooleanField(default = False)
    sittayma = models.BooleanField(default= True)
    video = models.URLField(max_length=500,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    longi = models.FloatField(null=True,blank=True)

    def __self__(self):
        return self.name

class honeymoon(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics',null=True,blank=True)
    small_desc = models.TextField(null=True,blank=True)
    big_desc = models.TextField(null=True,blank=True)  
    price = models.IntegerField(null=True,blank=True)
    offer = models.BooleanField(default = False)
    sittayma = models.BooleanField(default= True)
    video = models.URLField(max_length=500,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    longi = models.FloatField(null=True,blank=True)
    def __self__(self):
        return self.name

class familyplaces(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics',null=True,blank=True)
    small_desc = models.TextField(null=True,blank=True)
    big_desc = models.TextField(null=True,blank=True)  
    price = models.IntegerField(null=True,blank=True)
    offer = models.BooleanField(default = False)
    sittayma = models.BooleanField(default= True)
    video = models.URLField(max_length=500,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    longi = models.FloatField(null=True,blank=True)
    def __self__(self):
        return self.name
class nationalparks(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics',null=True,blank=True)
    small_desc = models.TextField(null=True,blank=True)
    big_desc = models.TextField(null=True,blank=True)  
    price = models.IntegerField(null=True,blank=True)
    offer = models.BooleanField(default = False)
    sittayma = models.BooleanField(default= True)
    video = models.URLField(max_length=500,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    longi = models.FloatField(null=True,blank=True)
    def __self__(self):
        return self.name

class budgetplaces(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics',null=True,blank=True)
    small_desc = models.TextField(null=True,blank=True)
    big_desc = models.TextField(null=True,blank=True)  
    price = models.IntegerField(null=True,blank=True)
    offer = models.BooleanField(default = False)
    sittayma = models.BooleanField(default= True)
    video = models.URLField(max_length=500,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    longi = models.FloatField(null=True,blank=True)
    def __self__(self):
        return self.name





















