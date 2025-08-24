# serializers.py for accounts app
from rest_framework import serializers 
from .models import CustomUser
from rest_framework.validators import ValidationError

class UserSerializer(serializers.ModelSerializer):
    """
    It converts CustomUser model instances to JSON (and vice-versa)
    for API requests and responses. It defines which fields are
    included and marks the role , username and email fields as read-only for security.
    """

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            role=validated_data.get('role', 'farmer'), 
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('password') 
        if 'role' in validated_data:
            request = self.context.get('request')
            if request and request.user.is_authenticated and request.user.role == 'admin':
                instance.role = validated_data.pop('role')
            else:
                validated_data.pop('role', None) 

        return super().update(instance, validated_data)


    def validate_role(self, value):
        request = self.context.get('request')
        if request and request.method == 'POST': 
            if value == 'admin' and (not request.user.is_authenticated or request.user.role != 'admin'):
                raise ValidationError("Only administrators can create new users with the 'admin' role.")
            if value not in [role[0] for role in CustomUser.ROLE_CHOICES]:
                 raise ValidationError(f"'{value}' is not a valid role.")
            
        return value
