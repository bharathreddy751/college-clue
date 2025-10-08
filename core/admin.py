from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Wishlist, University
#from .models import StudentRegistration  # adjust model name if different
from .models import Alumni # <-- Import the Alumni model

# ... your other admin registrations ...
admin.site.register(Alumni)

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
# admin.site.register(Wishlist)
from django.contrib import admin

# Register your models here.


class WishlistInline(admin.StackedInline):
    """
    Inline for the Wishlist model, displayed on the User admin page.
    """
    model = Wishlist
    can_delete = False
    verbose_name_plural = 'Wishlist'
    filter_horizontal = ('universities',)  # Provides a nice multi-select widget


# Unregister the default User admin to register our custom one
try:
    admin.site.unregister(User)
except admin.exceptions.NotRegistered:
    pass


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    """
    A custom User admin class that includes the WishlistInline.
    """
    inlines = (WishlistInline,)

    # You can add the wishlist count to the user list view if you wish
    list_display = BaseUserAdmin.list_display + ('get_wishlist_count',)

    def get_wishlist_count(self, obj):
        try:
            return obj.wishlist.universities.count()
        except Wishlist.DoesNotExist:
            return 0

    get_wishlist_count.short_description = 'Wishlist Count'




