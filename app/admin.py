from django.contrib import admin

# Register your models here.
from .models import Category,Sub_Category,Brands,Product

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Brands)
admin.site.register(Product)