from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # Add your custom fields
    full_name = models.CharField(max_length=150, blank=True)

    # Remove the email field override since AbstractUser already has it
    # Remove the groups and user_permissions overrides unless absolutely necessary

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
# ---------------------------
# 2. University
# ---------------------------
class University(models.Model):
    name = models.CharField(max_length=100)
    accreditation = models.CharField(max_length=200, blank=True)
    # alumni = models.TextField(blank=True)
    average_salary = models.CharField(max_length=50, blank=True)
    campus_size = models.CharField(max_length=50, blank=True)
    tuition = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=50, blank=True)
    undergraduate_enrollment = models.CharField(max_length=50, blank=True)
    graduate_enrollment = models.CharField(max_length=50, blank=True)
    financial_aid_available = models.BooleanField(default=False)
    established_year = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    password = models.CharField(max_length=50, blank=True)
    study_abroad_programs = models.BooleanField(default=False)
    registration_deadline = models.DateField(null=True, blank=True, help_text="The last date for student registration.")

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    """
    A model to represent a user's personal wishlist of universities.
    A user can only have one wishlist.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    universities = models.ManyToManyField(University, blank=True, related_name='wishlisted_by')

    def __str__(self):
        return f"Wishlist for {self.user.username}"

# ---------------------------
# 3. University Courses Offered
# ---------------------------
class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='courses')
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.university.name} - {self.course_name}"


# ---------------------------
# 4. Campus Facilities
# ---------------------------
class Facility(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='facilities')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.university.name} - {self.name}"


# ---------------------------
# 5. Nearby Restaurants
# ---------------------------
class Restaurant(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.university.name} - {self.name}"


# ---------------------------
# 6. Nearby Hangout Areas
# ---------------------------
class Hangout(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='hangouts')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.university.name} - {self.name}"


# ---------------------------
# 7. Nearby Paying Guests (PGs)
# ---------------------------
class PayingGuest(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='pgs')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    food = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    rent = models.CharField(max_length=10)
    password = models.CharField(max_length=50, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.university.name}"


class PGFacility(models.Model):
    pg = models.ForeignKey(PayingGuest, on_delete=models.CASCADE, related_name='facilities')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pg.name} - {self.name}"


# ---------------------------
# 8. Reviews
# ---------------------------
class Review(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField()
    timestamp = models.BigIntegerField()
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.university.name} - {self.user_name}"


# ---------------------------
# 9. Recruiters / Placements
# ---------------------------
class Recruiter(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='recruiters')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.university.name}"


# ---------------------------
# 10. Placement Record
# ---------------------------
class PlacementRecord(models.Model):
    university = models.OneToOneField(University, on_delete=models.CASCADE, related_name='placement_record')
    average_salary = models.CharField(max_length=50)
    placement_percentage = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.university.name} - {self.placement_percentage}"


# ---------------------------
# 11. Distance to Transport
# ---------------------------
class Transport(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='transports')
    type = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.university.name} - {self.type}"


# ---------------------------
# 12. Location Choices
# ---------------------------
class AvailableLocation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ---------------------------
# 13. Registration
# ---------------------------
class Registration(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='registrations')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Refers to the active user model
        on_delete=models.CASCADE,
            # Or models.SET_NULL, null=True, blank=True if registration can exist without a user
        related_name='registrations',
        null=True,  # Make it nullable for existing data or if registration can be anonymous
        blank=True  # Allow blank in forms
        )
    # Replaced course_category and course_option with available_courses
    available_courses = models.ForeignKey(
        UniversityCourse,
        on_delete=models.SET_NULL, # Consider what should happen if the course is deleted
        null=True,
        blank=True
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.university.name}"




class Alumni(models.Model):
    # CORRECTED: Changed 'College' to 'University' to match your actual model name
    university = models.ForeignKey('University', on_delete=models.CASCADE, related_name='alumni')

    name = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    image = models.ImageField(upload_to='alumni_photos/')
    current_company = models.CharField(max_length=100, blank=True)
    current_position = models.CharField(max_length=100, blank=True)
    testimonial = models.TextField(blank=True)
    linkedin_profile_url = models.URLField(blank=True)

    def __str__(self):
        # CORRECTED: Changed 'university.clg_name' to 'university.name'
        return f"{self.name} ({self.university.name})"