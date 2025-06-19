from rest_framework import serializers
from .models import Studio, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ['created_at']


class StudioSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)
    owner_email = serializers.EmailField(source='owner.email', read_only=True)

    class Meta:
        model = Studio
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']