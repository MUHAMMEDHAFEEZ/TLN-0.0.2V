from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import UserRole  # Only import UserRole from accounts models

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'role', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            role=validated_data['role'],
            password=validated_data['password']
        )
        return user

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    full_name = serializers.CharField(max_length=100)
    role = serializers.ChoiceField(choices=UserRole.choices, default=UserRole.CLIENT)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['full_name'] = self.validated_data.get('full_name', '')
        data['role'] = self.validated_data.get('role', UserRole.CLIENT)
        return data