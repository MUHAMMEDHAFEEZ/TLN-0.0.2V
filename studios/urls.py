from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudioViewSet, LocationViewSet, LocationAvailabilityView

router = DefaultRouter()
router.register(r'studios', StudioViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = router.urls + [
    path('locations/<int:pk>/availability/',
         LocationAvailabilityView.as_view(), 
         name='location-availability'),
]