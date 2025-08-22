from rest_framework import serializers # pyright: ignore[reportMissingImports]
from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
        """
    This prepares Sales records for the API, converting them to and from JSON.
    It displays the product's name, calculates the total sale amount automatically,
    and sets the sale date and total amount as read-only fields.
    """
        product_name = serializers.ReadOnlyField(source='product.name') # Display product name instead of product ID
        total_sale_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

        class Meta:
            model = Sale
            fields = ['id', 'product', 'product_name', 'quantity_sold', 'price_per_unit', 'total_sale_amount', 'date_sold']
            # 'date_sold' is auto-generated, 'total_sale_amount' is calculated
            read_only_fields = ['date_sold', 'total_sale_amount']