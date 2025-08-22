from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Product(models.Model):
    """This model represents an entry for every product produced or sold on the farm.
    It keeps track of the product details and the user who added it.
    """
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50, default='units')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
