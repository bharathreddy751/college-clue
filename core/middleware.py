from django.contrib.auth import logout
from django.utils import timezone


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Check if the session has a custom last activity timestamp
            if 'last_activity' in request.session:
                last_activity_str = request.session['last_activity']
                last_activity = timezone.datetime.fromisoformat(last_activity_str)

                # Set a custom timeout duration, e.g., 30 minutes
                timeout_duration = timezone.timedelta(minutes=30)

                # If the last activity was longer than the timeout, log the user out
                if (timezone.now() - last_activity) > timeout_duration:
                    logout(request)
                    return self.get_response(request)

            # Update the last activity timestamp on every request
            request.session['last_activity'] = timezone.now().isoformat()

        response = self.get_response(request)
        return response