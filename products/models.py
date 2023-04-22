from django.db import models
from users.models import Seller 
# Create your models here.

class Product(models.Model):
    productname=models.CharField(max_length=50)
    amountavailable=models.IntegerField()
    cost=models.DecimalField(max_digits=5,decimal_places=2)
    sellerid=models.ManyToManyField("users.Seller")
    