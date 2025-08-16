from rest_framework import serializers
from django.contrib.auth import authenticate
from core.models import (
    User, University, UniversityCourse, Facility, Restaurant,
    Hangout, PayingGuest, PGFacility, Review, Recruiter,
    PlacementRecord, Transport, AvailableLocation, Registration
)
class UserRegistrationSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'username', 'email', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data['full_name'],
            username=validated_data['email']  # Using email as username
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class UniversityCourseSerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name', read_only=True)

    class Meta:
        model = UniversityCourse
        fields = '__all__'


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class HangoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hangout
        fields = '__all__'


class PGFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PGFacility
        fields = '__all__'


class PayingGuestSerializer(serializers.ModelSerializer):
    facilities = PGFacilitySerializer(many=True, read_only=True)

    class Meta:
        model = PayingGuest
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'


class PlacementRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementRecord
        fields = '__all__'


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'


class AvailableLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableLocation
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name', read_only=True)
    available_course_name = serializers.CharField(source='available_courses.course_name', read_only=True)

    class Meta:
        model = Registration
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }