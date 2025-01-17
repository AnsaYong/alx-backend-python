import logging, time
from datetime import datetime
from django.http import HttpResponseForbidden
from collections import defaultdict


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


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_message_count = defaultdict(list)  # Track messages by IP

    def __call__(self, request):
        if (
            request.method == "POST" and "/chat/" in request.path
        ):  # Assuming chat messages are sent via POST
            ip = self.get_client_ip(request)
            current_time = time.time()

            # Filter out messages older than 1 minute
            self.ip_message_count[ip] = [
                timestamp
                for timestamp in self.ip_message_count[ip]
                if current_time - timestamp < 60
            ]

            # Check if the number of messages exceeds the limit
            if len(self.ip_message_count[ip]) >= 5:
                return HttpResponseForbidden(
                    "Message limit exceeded. Please wait a while before sending more messages."
                )

            # Add the current message timestamp
            self.ip_message_count[ip].append(current_time)

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
