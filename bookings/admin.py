from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'start_time', 'end_time', 'created_at')
    list_filter = ('location', 'start_time')
    search_fields = ('user__email',)
