from django.db import models
from products.models import Product
from accounts.models import CustomUser

# Create your models here.
class Sale(models.Model):
    """This model represents the record of each time a product on the farm is sold.
    It captures details about the sale, including the product sold, quantity, price,
    and the user who made the sale. A transaction history, basically.
    """

    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True, blank=True, related_name='sales')
    quantity_sold = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    date_sold = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sales')

    def total_amount_sold(self):
        return self.quantity_sold * self.price_per_unit

    def __str__(self):
        if self.product:
            product_name = self.product.name
        else:
            product_name = "Unknown Product"
        return f"Sale of {self.quantity_sold} {product_name} on {self.date_sold.strftime('%Y-%m-%d')}"