from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """A user setup for the farmtracker that distinguishes different roles of the user of the app
    This helps manage what each user can do on the app.
    """
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
        ('customer', 'Customer'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default = 'Farmer')
    
    def __str__(self):
        return f"{self.username} ({self.role})"
