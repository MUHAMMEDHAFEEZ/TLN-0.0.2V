from django.contrib import admin
from .models import Studio, Location


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    search_fields = ('name', 'owner__email')
    list_filter = ('created_at',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'studio', 'floor', 'is_active')
    search_fields = ('name', 'studio__name')
    list_filter = ('is_active', 'studio')


