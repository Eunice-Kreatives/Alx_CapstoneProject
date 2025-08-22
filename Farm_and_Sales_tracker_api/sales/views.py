from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminOrFarmer
from .models import Sale
from .serializers import SaleSerializer

# Create your views here.
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all() # Base queryset
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated, IsAdminOrFarmer]

    def get_queryset(self):
        """
            Filters sales based on the user's role:
            - Farmers see sales related to their own products.
            - Admins see all sales.
            - Customers generally do NOT see sales directly (unless linked to their own orders, not implemented here).
            """
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'farmer':
                    # Farmers see sales where the product belongs to them
                return Sale.objects.filter(product__user=user).order_by('-date_sold')
            elif user.role == 'admin':
                    # Admins see and manage all sales
                return Sale.objects.all().order_by('-date_sold')
            elif user.role == 'customer':
                    # Customers typically should not view sales records directly.
                    # If they placed orders, they'd view an 'Order' model's history.
                return Sale.objects.none() # Customers see no sales by default
        return Sale.objects.none() # Unauthenticated users see no sales

    def perform_create(self, serializer):
        """
        Assigns the logged-in user as the recorder of a new sale.
        This will only be called if IsAdminOrFarmer permission allows (i.e., user is Admin or Farmer).
        """
        serializer.save(user=self.request.user)
    
