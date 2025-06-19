from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Studio(models.Model):
    STUDIO_TYPES = [
        ('CYCLORAMA', 'Cyclorama Studio'),
        ('KITCHEN', 'Kitchen Studio'),
        ('OPEN_SPACE', 'Open Space Studio'),
        ('PODCAST', 'Podcast Studio'),
        ('AUDIO', 'Audio Recording Studio'),
        ('OUTDOOR', 'Outdoor Studio'),
        ('GREEN_SCREEN', 'Green Screen Studio'),
        ('BLACK_BOX', 'Black Box Studio'),
        ('LIFESTYLE', 'Lifestyle Studio'),
        ('NATURAL_LIGHT', 'Natural Light Studio'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='studios')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    studio_type = models.CharField(max_length=50, choices=STUDIO_TYPES)
    size = models.CharField(max_length=100, blank=True)
    capacity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    attributes = models.JSONField(default=dict)  # For type-specific attributes
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_studio_type_display()})"


class Location(models.Model):
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=255)
    floor = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.studio.name})"