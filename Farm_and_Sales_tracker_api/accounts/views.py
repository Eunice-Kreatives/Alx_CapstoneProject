from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('username')
    serializer_class = UserSerializer
    
    def get_persmissions(self):
        """
        Sets permissions based on the action:
        - Any user can create an account (registration).
        - Authenticated users can retrieve, update, or partially update their OWN profile.
        - Only Admins can list all users or destroy any user.
        """
        if self.action == 'create': 
            return [] 
        elif self.action in ['retrieve', 'update', 'partial_update']:
            return [IsAuthenticated()]
        elif self.action == 'list' or self.action == 'destroy':
            return [IsAdminUser()]
        return [IsAuthenticated()] 
    