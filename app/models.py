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
    Category = models.ForeignKey(Category, on_delete=models.CASCADE,null = False)
    Sub_Category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null = False)
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
    
    
    

"""code for  creating a new user if user already exits then it will show a message that user already exists """ 
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,label='email',error_messages={"exists":"this mail is already exists"})

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'

    def Save(self,commit = True):
        user = super(UserCreateForm,self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user
    
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']
    


"""code for getting user information in contact page where it will  be analysed and after that it will be assignwed to various department"""
class ContactFormSubmission(models.Model):
    firstname  = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    subject = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    now = datetime.datetime.now()
    today = datetime.datetime.today()
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.now}"
        
    class Meta:
        verbose_name_plural = 'Contact Form data'
        ordering = ['-submission_date']


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'profile')
    name = models.CharField(max_length=255,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
