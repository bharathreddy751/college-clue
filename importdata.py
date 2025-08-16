import json
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject2.settings')
django.setup()

from core.models import (
    User, CourseCategory, CourseOption, University,
    UniversityCourse, Facility, Restaurant, Hangout,
    PayingGuest, PGFacility, Review, Recruiter, PlacementRecord,
    Transport, AvailableLocation
)

# Load JSON data
with open('college-clue-default-rtdb-export.json', 'r') as file:
    data = json.load(file)

# Load Users
for user in data.get('users', {}).values():
    User.objects.get_or_create(
        email=user.get('email', ''),
        full_name=user.get('fullName', ''),
        password=user.get('password', '')
    )

# Load Courses
for course in data.get('courses', []):
    category, _ = CourseCategory.objects.get_or_create(name=course['category'])
    for option in course.get('options', []):
        CourseOption.objects.get_or_create(category=category, name=option)

# Load Available Locations
for location in data.get('location', []):
    AvailableLocation.objects.get_or_create(name=location)

# Load Universities and related data
for uni_name, u in data.get('universities', {}).items():
    uni, _ = University.objects.get_or_create(
        name=uni_name,
        location=u.get('Location', ''),
        accreditation=u.get('Accreditation', ''),
        tuition=u.get('Tuition (In-state)', ''),
        website=u.get('Website', ''),
        average_salary=u.get('Average Salary', ''),
        #placement_percentage=u.get('Placement Percentage', ''),
        image_url=u.get('imageURL', ''),
        type=u.get('Type', ''),
        campus_size=u.get('Campus Size', ''),
        undergraduate_enrollment=u.get('Undergraduate Enrollment', ''),
        graduate_enrollment=u.get('Graduate Enrollment', ''),
        financial_aid_available=u.get('Financial Aid Available', '') == "Yes",
        established_year=str(u.get('Established Year', '')),
        password=u.get('password', ''),
        study_abroad_programs=u.get('Study Abroad Programs', '') == "Yes",
        latitude=u.get('latitude', 0.0),
        longitude=u.get('longitude', 0.0)
    )

    # University Courses Offered
    for course_name in u.get('Courses Offered', []):
        UniversityCourse.objects.get_or_create(university=uni, course_name=course_name)

    # Campus Facilities
    for f in u.get('Campus Facilities', []):
        Facility.objects.get_or_create(university=uni, name=f)

    # Restaurants
    for r in u.get('Nearby Restaurants', []):
        Restaurant.objects.get_or_create(university=uni, name=r)

    # Hangout Areas
    if isinstance(u.get('Nearby Hangout Areas', []), list):
        for h in u.get('Nearby Hangout Areas', []):
            Hangout.objects.get_or_create(university=uni, name=h)

    # PGs
    for pg in u.get('Nearby Paying Guests', []):
        if isinstance(pg, dict):
            pg_obj, _ = PayingGuest.objects.get_or_create(
                university=uni,
                name=pg.get('Name', ''),
                address=pg.get('Address', ''),
                contact=pg.get('Contact', ''),
                food=pg.get('Food', ''),
                gender=pg.get('Gender', ''),
                rent=pg.get('Rent', ''),
                password=pg.get('password', ''),
                latitude=pg.get('latitude', 0.0),
                longitude=pg.get('longitude', 0.0)
            )
            for facility in pg.get('Facilities', []):
                PGFacility.objects.get_or_create(pg=pg_obj, name=facility)

    # Reviews
    for review in u.get('Reviews', {}).values():
        Review.objects.get_or_create(
            university=uni,
            rating=review.get('rating', 0),
            text=review.get('text', ''),
            timestamp=review.get('timestamp', 0),
            user_name=review.get('userName', '')
        )

    # Recruiters
    for r in u.get('Top Recruiters', []):
        Recruiter.objects.get_or_create(university=uni, name=r)

    # Placement Record
    if 'Placement Record' in u:
        pr = u['Placement Record']
        PlacementRecord.objects.get_or_create(
            university=uni,
            average_salary=pr.get('Average Salary', ''),
            placement_percentage=pr.get('Placement Percentage', '')
        )

    # Transport Info
    for k, v in u.get('Distance to Transport', {}).items():
        Transport.objects.get_or_create(
            university=uni,
            type=k,
            distance=v
        )

print("✅ All data imported successfully.")
