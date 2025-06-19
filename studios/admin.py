from django.contrib import admin
from .models import Studio, Location
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'studio_type', 'price_per_hour', 'is_active')
    list_filter = ('studio_type', 'is_active')
    search_fields = ('name', 'owner__email')

    # Add this method to fix the owner selection
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "owner":
            kwargs["queryset"] = User.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'studio', 'floor', 'is_active')
    list_filter = ('is_active', 'studio')
    search_fields = ('name', 'studio__name')