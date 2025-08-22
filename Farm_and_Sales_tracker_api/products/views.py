from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminOrFarmer
from .models import Product
from .serializers import ProductSerializer 
from rest_framework import viewsets

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrFarmer]

    def get_queryset(self):
        """
        Filters products based on the user's role:
        - Farmers see only their own products.
        - Admins see all products.
        - Customers see all products (read-only for them via permission_classes).
        """
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'farmer':
                    # Farmers manage their own products
                return Product.objects.filter(user=user).order_by('name')
            elif user.role == 'admin':
                    # Admins see and manage all products
                return Product.objects.all().order_by('name')
            elif user.role == 'customer':
                return Product.objects.all().order_by('name')
            return Product.objects.none()

        def perform_create(self, serializer):
            """
            Assigns the logged-in user as the owner of a new product.
            This will only be called if IsAdminOrFarmer permission allows (i.e., user is Admin or Farmer).
            """
            serializer.save(user=self.request.user)
    
    