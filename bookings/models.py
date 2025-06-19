from django.db import models
from django.conf import settings
from studios.models import Location
from django.core.exceptions import ValidationError


class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]

    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings_created'
    )
    client_name = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=20)
    client_email = models.EmailField(blank=True, null=True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='bookings'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    equipment = models.JSONField(default=list)  # Store equipment as JSON
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    def clean(self):
        # Validate time slot
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be after start time")

        # Check for overlapping bookings (exclude cancelled and completed)
        overlapping = Booking.objects.filter(
            location=self.location,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(
            status__in=['CANCELLED', 'COMPLETED']
        ).exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError("This time slot conflicts with an existing booking")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client_name} - {self.location} ({self.start_time} to {self.end_time})"