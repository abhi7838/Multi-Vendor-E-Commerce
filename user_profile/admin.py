from django.contrib import admin
from .models import *


admin.site.register(CartItem)

# Register your models here. copied from home_admin
admin.site.register(Product)
admin.site.register(Brands)
admin.site.register(Sub_Category)
admin.site.register(Category)
