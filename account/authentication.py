from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend

class UsernameOrEmailBackend(BaseBackend):
    def authenticate(self, request, username_or_email=None, password=None):
        try:
            # Check if the username_or_email is an email address
            user = User.objects.get(email=username_or_email)
        except User.DoesNotExist:
            # If not, try to get the user by username
            try:
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                return None

        # Check the password
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
