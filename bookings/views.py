from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated


class BookingViewSet(viewsets.ModelViewSet):
    # Add queryset attribute to fix router issue
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['STAFF', 'OWNER']:
            return Booking.objects.filter(agent=user)
        return Booking.objects.filter(client_email=user.email)

    def perform_create(self, serializer):
        serializer.save(agent=self.request.user)