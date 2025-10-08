
# DjangoProject2/core/views.py
from allauth.account.views import SignupView
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import University, UniversityCourse # Import UniversityCourse
from .forms import RegistrationForm
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings # Make sure settings is imported if you're using it for email
# REMOVE THIS LINE: from allauth.account import views as allauth_views # <--- REMOVE THIS LINE IF NOT USED FOR OTHER THINGS
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import REDIRECT_FIELD_NAME # <--- KEEP THIS LINE
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import University, Wishlist
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.shortcuts import render, get_object_or_404
from .models import Alumni, University



def home(request):
    universities = University.objects.all()

    # Get all raw locations first
    raw_locations = University.objects.values_list('location', flat=True)

    cleaned_locations = set() # Use a set to automatically handle uniqueness
    for loc in raw_locations:
        if loc: # Ensure location is not empty
            # Split by comma and take the first part, then strip whitespace
            city = loc.split(',')[0].strip()
            if city: # Ensure the cleaned city is not empty
                cleaned_locations.add(city)

    # Convert the set to a sorted list for the template
    unique_locations = sorted(list(cleaned_locations))

    return render(request, 'core/listofuniversities.html', {
        'universities': universities,
        'unique_locations': unique_locations # Pass the cleaned, unique locations
    })

def university_detail(request, pk):
    university = get_object_or_404(University, pk=pk)
    courses_offered = UniversityCourse.objects.filter(university=university)
    return render(request, 'core/universitydetails.html', {'university': university, 'courses_offered': courses_offered})


@login_required(login_url='account_login')
def university_register(request, pk):
    university = get_object_or_404(University, pk=pk)

    if request.method == 'POST':
        form = RegistrationForm(request.POST, university=university)

        if form.is_valid():
            registration = form.save(commit=False)
            registration.university = university
            registration.save()

            subject = f"Registration Successful at {university.name}"
            message = f"""
Dear {registration.first_name},

Thank you for registering at {university.name}!
You have registered for the course: {registration.available_courses.course_name}.

We have received your application and will process it soon.

Best regards,
College Clue Team
"""
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [registration.email], fail_silently=False)
            except Exception as e:
                print(f"❌ Email failed: {e}")

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})

            from django.contrib import messages
            messages.success(request, "You have successfully registered for the university!")
            return render(request, 'core/register.html', {
                'form': RegistrationForm(university=university),
                'university': university,
                'success': True
            })
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            else:
                from django.contrib import messages
                messages.error(request, "Please correct the errors below.")

    else: # GET request
        form = RegistrationForm(university=university)

    return render(request, 'core/register.html', {
        'form': form,
        'university': university,
        'success': False
    })

def compare_colleges(request):
    ids = request.GET.get('ids', '')
    id_list = [int(pk) for pk in ids.split(',') if pk.isdigit()]
    universities = University.objects.filter(id__in=id_list)
    return render(request, 'core/compare.html', {'universities': universities})

def landing(request):
    return render(request, 'core/landing.html', {'request': request})


def login(request):
    # Get the 'next' URL parameter from the GET request
    # Use the directly imported REDIRECT_FIELD_NAME
    redirect_field_name = REDIRECT_FIELD_NAME # <--- THIS IS THE CORRECTED LINE
    redirect_field_value = request.GET.get(redirect_field_name)

    context = {
        'request': request,
        'redirect_field_name': redirect_field_name,
        'redirect_field_value': redirect_field_value,
    }
    return render(request, 'core/login.html', context)


class CustomSignupView(SignupView):
    def form_valid(self, form):
        # Create user but don't login
        self.user = form.save(self.request)
        return redirect('account_login')


def heartbeat(request):
    return JsonResponse({"status": "ok"})


@login_required(login_url='account_login')
def my_wishlists(request):
    """
    Renders the wishlist page for the currently logged-in user.
    """
    try:
        # Debug: Check user and wishlist
        print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")

        # Get or create wishlist for the user
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        universities = wishlist.universities.all()

        # Debug: Print what's in the wishlist
        print(f"Wishlist universities: {[uni.name for uni in universities]}")
        print(f"Wishlist count: {universities.count()}")

    except Exception as e:
        # Log the error and return empty list
        print(f"Error retrieving wishlist: {e}")
        universities = []

    return render(request, 'core/wishlist.html', {'universities': universities})
@require_POST
@login_required
def add_to_wishlist(request):
    """
    Adds a university to the user's wishlist via an AJAX POST request.
    """
    try:
        data = json.loads(request.body)
        university_id = data.get('university_id')
        university = get_object_or_404(University, pk=university_id)

        # Get or create the wishlist for the current user.
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist.universities.add(university)

        return JsonResponse({'success': True, 'message': f'Added {university.name} to wishlist.'})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON.'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@require_POST
@login_required
def remove_from_wishlist(request):
    """
    Removes a university from the user's wishlist via an AJAX POST request.
    """
    try:
        data = json.loads(request.body)
        university_id = data.get('university_id')
        university = get_object_or_404(University, pk=university_id)

        # Get the wishlist for the current user.
        wishlist = get_object_or_404(Wishlist, user=request.user)
        wishlist.universities.remove(university)

        return JsonResponse({'success': True, 'message': f'Removed {university.name} from wishlist.'})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON.'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


def alumni_list_view(request, university_pk):
    # CORRECTED: Changed 'College' to 'University'
    university = get_object_or_404(University, pk=university_pk)

    alumni_list = university.alumni.all()
    context = {
        'university': university,
        'alumni_list': alumni_list
    }
    return render(request, 'alumni_list.html', context)

def alumni_detail_view(request, alumnus_pk):
    alumnus = get_object_or_404(Alumni, pk=alumnus_pk)
    context = {
        'alumnus': alumnus
    }
    return render(request, 'alumni_detail.html', context)