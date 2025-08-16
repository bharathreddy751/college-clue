from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, UniversityViewSet, UniversityCourseViewSet,
    FacilityViewSet, RestaurantViewSet, HangoutViewSet,
    PayingGuestViewSet, PGFacilityViewSet, ReviewViewSet,
    RecruiterViewSet, PlacementRecordViewSet, TransportViewSet,
    AvailableLocationViewSet, RegistrationViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'universities', UniversityViewSet)
router.register(r'university-courses', UniversityCourseViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'hangouts', HangoutViewSet)
router.register(r'paying-guests', PayingGuestViewSet)
router.register(r'pg-facilities', PGFacilityViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'recruiters', RecruiterViewSet)
router.register(r'placement-records', PlacementRecordViewSet)
router.register(r'transports', TransportViewSet)
router.register(r'available-locations', AvailableLocationViewSet)
router.register(r'registrations', RegistrationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]