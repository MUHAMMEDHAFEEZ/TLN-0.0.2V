from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import time, timedelta
from .models import Studio, Location
from bookings.models import Booking
from .serializers import StudioSerializer, LocationSerializer


class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.filter(is_active=True)
    serializer_class = StudioSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        studio_type = self.request.query_params.get('type')
        if studio_type:
            queryset = queryset.filter(studio_type=studio_type)
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price_per_hour__gte=min_price)
        if max_price:
            queryset = queryset.filter(price_per_hour__lte=max_price)
        return queryset


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.filter(is_active=True)
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        studio_id = self.request.query_params.get('studio')
        if studio_id:
            queryset = queryset.filter(studio_id=studio_id)
        return queryset


class LocationAvailabilityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        location = get_object_or_404(Location, id=pk, is_active=True)

        date_str = request.query_params.get('date')
        if date_str:
            try:
                date = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                return Response(
                    {"error": "Invalid date format. Use YYYY-MM-DD."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            date = timezone.now().date()

        bookings = Booking.objects.filter(
            location=location,
            start_time__date=date,
            status__in=['CONFIRMED', 'PENDING']
        ).order_by('start_time')

        slots = []
        # Fix timezone handling
        start_datetime = timezone.make_aware(
            timezone.datetime.combine(date, time(9, 0)))
        end_datetime = timezone.make_aware(
            timezone.datetime.combine(date, time(21, 0)))

        current = start_datetime
        while current < end_datetime:
            slot_end = current + timedelta(hours=1)

            is_available = True
            for booking in bookings:
                if booking.start_time < slot_end and booking.end_time > current:
                    is_available = False
                    break

            if is_available:
                slots.append({
                    'start': current,
                    'end': slot_end
                })

            current = slot_end

        return Response({
            'location': location.name,
            'date': date,
            'available_slots': slots
        })