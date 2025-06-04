from django.db import models
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from  django.conf import settings
from django.contrib.auth import get_user_model
import datetime

# Create your models here.
#copied from home_models
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
    print(models.Model)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null = True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    #ensure that user doesn't have the same product multiple time 
    #unless user is null, which means its a session cart item
 

    def __str__(self):
        if self.user:
            return f"{self.quantity} x {self.Poduct.name} x {self.user.username}"
        return f"{self.quantity} x {self.Product.name} (anonymous Cart)"
    
    @property
    def total_item_price(self):
        return self.quantity*self.product.price
    

#class for adding product in cart 
class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1,initial=1)
    product_id = forms.IntegerField(widget=forms.HiddenInput())

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.EmailField("")
    address = models.CharField(max_length=199)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)

    class meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Oder{self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='item', on_delete= models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_item',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)

    class Meta:
        unique_together = ('order','product')


    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price*self.quantity
    
