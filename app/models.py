from django.db import models

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
    Category = models.ForeignKey(Category, on_delete=models.CASCADE,null = 'False')
    Sub_Category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null = 'False')
    image = models.ImageField(upload_to='E_shop/img')
    name  = models.CharField(max_length=150)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
