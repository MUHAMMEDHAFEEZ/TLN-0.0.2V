from django.db import models
from django.conf import settings
from studios.models import Location

class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings'
    )
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='bookings'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} booking at {self.location} from {self.start_time} to {self.end_time}"
