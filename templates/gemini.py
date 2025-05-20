# your_app_name/models.py
from django.db import models
from django.conf import settings # Import settings to reference AUTH_USER_MODEL
from django.contrib.auth import get_user_model # A safer way to get the User model

# Assuming you already have Category and Sub_Category defined
# from .category_model import Category # Adjust if your Category model is in a different file
# from .subcategory_model import Sub_Category # Adjust if your Sub_Category model is in a different file

# --- Your Existing Product Model (with important corrections) ---
class Product(models.Model):
    # Corrected 'null' and 'blank' to boolean False, and price to DecimalField
    Category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True) # Assuming 'Category' is defined elsewhere
    Sub_Category = models.ForeignKey('Sub_Category', on_delete=models.CASCADE, null=True, blank=True) # Assuming 'Sub_Category' is defined elsewhere
    image = models.ImageField(upload_to='E_shop/img', blank=True, null=True) # Added blank/null for images
    name = models.CharField(max_length=150)
    # IMPORTANT: Changed to DecimalField for accurate price calculation
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    # Add this method if you need to display a default image when none is uploaded
    def get_image_url(self):
        if self.image:
            return self.image.url
        return '/static/images/default_product.png' # Path to a default image in your static files


# --- NEW: CartItem Model ---
class CartItem(models.Model):
    # Use get_user_model() to correctly reference the User model (custom or default)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    # null=True, blank=True allows for anonymous session carts to be merged later
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user doesn't have the same product multiple times in their cart
        # (unless user is null, which means it's a session cart item)
        unique_together = ('user', 'product')
        ordering = ['-date_added'] # Order cart items by most recently added

    def __str__(self):
        if self.user:
            return f"{self.quantity} x {self.product.name} for {self.user.username}"
        return f"{self.quantity} x {self.product.name} (Anonymous Cart)"

    @property
    def total_item_price(self):
        """Calculates the total price for this specific cart item (quantity * product price)."""
        return self.quantity * self.product.price