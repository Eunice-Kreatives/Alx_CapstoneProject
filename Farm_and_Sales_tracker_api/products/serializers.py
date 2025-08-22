from rest_framework import serializers 
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    This translates Product model data into a format that can be easily sent
    or received by the API (like JSON). It also makes sure the 'user' field
    is automatically handled and shows the username, and sets creation/update
    timestamps as read-only.
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']