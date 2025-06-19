from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('agent', 'client_name', 'location', 'start_time', 'end_time', 'status')
    list_filter = ('location', 'start_time', 'status')
    search_fields = ('agent__email', 'client_name', 'client_phone')