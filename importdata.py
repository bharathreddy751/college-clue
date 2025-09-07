import json
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject2.settings')
django.setup()

from core.models import (
    User, University, UniversityCourse, Facility,
    Restaurant, Hangout, PayingGuest, PGFacility,
    Review, Recruiter, PlacementRecord, Transport,
    AvailableLocation
)
from django.contrib.auth.hashers import make_password

# Load JSON data
with open('college-clue-default-rtdb-export.json', 'r') as file:
    data = json.load(file)

print("Starting data import...")

# Load Users
print("Importing users...")
for user_id, user_data in data.get('users', {}).items():
    try:
        # Create user with hashed password
        user, created = User.objects.get_or_create(
            username=user_id,  # Using the Firebase user ID as username
            defaults={
                'email': user_data.get('email', ''),
                'full_name': user_data.get('fullName', ''),
                'password': make_password(user_data.get('password', '')),
            }
        )
        if created:
            print(f"Created user: {user.username}")
    except Exception as e:
        print(f"Error creating user {user_id}: {e}")

# Load Available Locations
print("Importing locations...")
for location in data.get('location', []):
    AvailableLocation.objects.get_or_create(name=location)

# Load Universities and related data
print("Importing universities...")
for uni_name, uni_data in data.get('universities', {}).items():
    try:
        # Create university
        uni, created = University.objects.get_or_create(
            name=uni_name,
            defaults={
                'location': uni_data.get('Location', ''),
                'accreditation': uni_data.get('Accreditation', ''),
                'alumni': uni_data.get('Alumni', ''),
                'average_salary': uni_data.get('Average Salary', ''),
                'campus_size': uni_data.get('Campus Size', ''),
                'tuition': uni_data.get('Tuition ', ''),  # Note the space in key
                'type': uni_data.get('Type', ''),
                'undergraduate_enrollment': uni_data.get('Undergraduate Enrollment', ''),
                'graduate_enrollment': uni_data.get('Graduate Enrollment', ''),
                'financial_aid_available': bool(uni_data.get('Financial Aid Available', False)),
                'established_year': str(uni_data.get('Established Year', '')),
                'website': uni_data.get('Website', ''),
                'image_url': uni_data.get('imageURL', ''),
                'latitude': float(uni_data.get('latitude', 0.0)),
                'longitude': float(uni_data.get('longitude', 0.0)),
                'password': uni_data.get('password', ''),
                'study_abroad_programs': bool(uni_data.get('Study Abroad Programs', False))
            }
        )

        if created:
            print(f"Created university: {uni_name}")

        # University Courses Offered
        for course_name in uni_data.get('Courses Offered', []):
            UniversityCourse.objects.get_or_create(
                university=uni,
                course_name=course_name
            )

        # Campus Facilities
        for facility_name in uni_data.get('Campus Facilities', []):
            Facility.objects.get_or_create(
                university=uni,
                name=facility_name
            )

        # Restaurants
        for restaurant_name in uni_data.get('Nearby Restaurants', []):
            Restaurant.objects.get_or_create(
                university=uni,
                name=restaurant_name
            )

        # Hangout Areas
        hangout_areas = uni_data.get('Nearby Hangout Areas', [])
        if isinstance(hangout_areas, list):
            for hangout_name in hangout_areas:
                Hangout.objects.get_or_create(
                    university=uni,
                    name=hangout_name
                )

        # Paying Guests (PGs)
        for pg_data in uni_data.get('Nearby Paying Guests', []):
            if isinstance(pg_data, dict):
                pg, pg_created = PayingGuest.objects.get_or_create(
                    university=uni,
                    name=pg_data.get('Name', ''),
                    defaults={
                        'address': pg_data.get('Address', ''),
                        'contact': pg_data.get('Contact', ''),
                        'food': pg_data.get('Food', ''),
                        'gender': pg_data.get('Gender', ''),
                        'rent': pg_data.get('Rent', ''),
                        'password': pg_data.get('password', ''),
                        'latitude': float(pg_data.get('latitude', 0.0)),
                        'longitude': float(pg_data.get('longitude', 0.0))
                    }
                )

                # PG Facilities
                for facility_name in pg_data.get('Facilities', []):
                    PGFacility.objects.get_or_create(
                        pg=pg,
                        name=facility_name
                    )

        # Reviews
        for review_id, review_data in uni_data.get('Reviews', {}).items():
            Review.objects.get_or_create(
                university=uni,
                rating=review_data.get('rating', 0),
                text=review_data.get('text', ''),
                timestamp=review_data.get('timestamp', 0),
                user_name=review_data.get('userName', '')
            )

        # Recruiters
        for recruiter_name in uni_data.get('Top Recruiters', []):
            Recruiter.objects.get_or_create(
                university=uni,
                name=recruiter_name
            )

        # Placement Record
        placement_data = uni_data.get('Placement Record', {})
        if placement_data:
            PlacementRecord.objects.get_or_create(
                university=uni,
                defaults={
                    'average_salary': placement_data.get('Average Salary', ''),
                    'placement_percentage': placement_data.get('Placement Percentage', '')
                }
            )

        # Transport Info
        transport_data = uni_data.get('Distance to Transport', {})
        if isinstance(transport_data, dict):
            for transport_type, distance in transport_data.items():
                Transport.objects.get_or_create(
                    university=uni,
                    type=transport_type,
                    distance=distance
                )

    except Exception as e:
        print(f"Error processing university {uni_name}: {e}")

print("✅ All data imported successfully!")