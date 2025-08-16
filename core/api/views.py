from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from core.models import (
    User, University, UniversityCourse, Facility, Restaurant,
    Hangout, PayingGuest, PGFacility, Review, Recruiter,
    PlacementRecord, Transport, AvailableLocation, Registration
)
from .serializers import (
    UserSerializer, UniversitySerializer, UniversityCourseSerializer,
    FacilitySerializer, RestaurantSerializer, HangoutSerializer,
    PayingGuestSerializer, PGFacilitySerializer, ReviewSerializer,
    RecruiterSerializer, PlacementRecordSerializer, TransportSerializer,
    AvailableLocationSerializer, RegistrationSerializer,
    UserRegistrationSerializer, UserLoginSerializer
)

class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint that allows users to register
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)

class UserLoginView(generics.GenericAPIView):
    """
    API endpoint that allows users to login
    """
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        })

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class UniversityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows universities to be viewed or edited
    """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filterset_fields = ['location', 'type']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UniversityCourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows university courses to be viewed or edited
    """
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FacilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows facilities to be viewed or edited
    """
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows restaurants to be viewed or edited
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HangoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hangout spots to be viewed or edited
    """
    queryset = Hangout.objects.all()
    serializer_class = HangoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PayingGuestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows paying guest accommodations to be viewed or edited
    """
    queryset = PayingGuest.objects.all()
    serializer_class = PayingGuestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PGFacilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PG facilities to be viewed or edited
    """
    queryset = PGFacility.objects.all()
    serializer_class = PGFacilitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RecruiterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recruiters to be viewed or edited
    """
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PlacementRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows placement records to be viewed or edited
    """
    queryset = PlacementRecord.objects.all()
    serializer_class = PlacementRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TransportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transport options to be viewed or edited
    """
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AvailableLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows available locations to be viewed or edited
    """
    queryset = AvailableLocation.objects.all()
    serializer_class = AvailableLocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows registrations to be viewed or edited
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]