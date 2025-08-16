
from .models import UniversityCourse, Registration
from django import forms

class RegistrationForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('', 'Select Gender'),  # Optional: A blank default option
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True) # Explicitly define gender as a ChoiceField

    class Meta:
        model = Registration
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'birth_date', 'gender',
            'available_courses'
        ]

    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    available_courses = forms.ModelChoiceField(
        queryset=UniversityCourse.objects.none(),  # Will be populated in __init__
        empty_label="Select a Course",
        label="Available Courses"
    )

    def __init__(self, *args, university=None, **kwargs):
        super().__init__(*args, **kwargs)

        if university:
            # Filter UniversityCourse objects for the given university
            self.fields['available_courses'].queryset = UniversityCourse.objects.filter(
                university=university
            ).order_by('course_name')
        else:
            # If no university is provided, the queryset will remain empty,
            # or you might want to set a default or raise an error depending on your logic.
            self.fields['available_courses'].queryset = UniversityCourse.objects.none()

        # If it's an instance (i.e., editing an existing registration),
        # ensure the current course is selected if it's available for the university.
        if self.instance.pk and self.instance.available_courses:
            if university and UniversityCourse.objects.filter(university=university, id=self.instance.available_courses.id).exists():
                self.fields['available_courses'].initial = self.instance.available_courses
            elif not university: # If no university is passed but an instance exists, maybe still show the current course.
                self.fields['available_courses'].initial = self.instance.available_courses