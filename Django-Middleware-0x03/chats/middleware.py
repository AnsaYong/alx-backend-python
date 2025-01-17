import logging
from datetime import datetime
from django.http import HttpResponseForbidden


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure logging
        logging.basicConfig(
            filename="requests.log", level=logging.INFO, format="%(message)s"
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().time()
        start_time = datetime.strptime("21:00", "%H:%M").time()  # 9:00 PM
        end_time = datetime.strptime("06:00", "%H:%M").time()  # 6:00 AM

        # Check if current time is outside the allowed window
        if current_time < end_time or current_time > start_time:
            return HttpResponseForbidden("Access denied: Outside allowed hours.")

        response = self.get_response(request)
        return response
