from django.db import models

# Create your models here.

class vendor(models.Model):
    name=models.CharField(max_length=100)
    shopName=models.CharField(max_length=100)
    shopAddress=models.CharField(max_length=100)
    ShopLicence=models.ImageField(upload_to='licence',blank=True)
    longitude=models.FloatField()
    latitude=models.FloatField()
    email=models.EmailField(max_length=100)
    phoneNo=models.IntegerField()
    password=models.CharField(max_length=100)
    confPass=models.CharField(max_length=100)
    is_approved=models.BooleanField(default=False)

class customer(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phoneNo=models.IntegerField()
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confPass=models.CharField(max_length=100)




