from django.contrib import admin
from .models import *
#from .models import StudentRegistration  # adjust model name if different


admin.site.register(User)
# admin.site.register(CourseCategory)
# admin.site.register(CourseOption)
admin.site.register(University)
admin.site.register(UniversityCourse)
admin.site.register(Facility)
admin.site.register(Restaurant)
admin.site.register(Hangout)
admin.site.register(PayingGuest)
admin.site.register(PGFacility)
admin.site.register(Review)
admin.site.register(Recruiter)
admin.site.register(PlacementRecord)
admin.site.register(Transport)
admin.site.register(AvailableLocation)
  # adjust model name if different
admin.site.register(Registration)

from django.contrib import admin

# Register your models here.






