# serializers.py for accounts app
from rest_framework import serializers 
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    It converts CustomUser model instances to JSON (and vice-versa)
    for API requests and responses. It defines which fields are
    included and marks the role , username and email fields as read-only for security.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name']
        read_only_fields = ['role', 'username', 'email'] 