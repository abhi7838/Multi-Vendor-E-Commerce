from django.db import models
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from  django.conf import settings
from django.contrib.auth import get_user_model
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Brands(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, blank=True)
    Sub_Category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null = True, blank=True)
    image = models.ImageField(upload_to='E_shop/img')
    name  = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        


        
class CartItem(models.Model): # for adding products in cart 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    #ensure that user doesn't have the same product multiple time 
    #unless user is null, which means its a session cart item
    unique_together = ('user','product')
    ordering = ['-date_added'] #order cart items by most recently added 

    def __str__(self):
        if self.user:
            return f"{self.quantity} x {self.Poduct.name} x {self.user.username}"
        return f"{self.quantity} x {self.Product.name} (anonymous Cart)"
    
    @property
    def total_item_price(self):
        return self.quantity*self.Product.price