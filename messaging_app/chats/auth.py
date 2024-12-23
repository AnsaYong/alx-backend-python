from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):
    """
    Custom JWT Authentication to add additional checks or logging.
    """

    def authenticate(self, request):
        # Call the parent class's authenticate method
        auth_result = super().authenticate(request)

        if auth_result is not None:
            user, token = auth_result
            # Perform additional checks or logging if needed
            print(f"User {user.username} authenticated successfully.")

        return auth_result
