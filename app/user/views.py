"""Views for the Create user API"""

from rest_framework.generics import CreateAPIView

from user.serializers import UserSerializer

class CreatUserView(CreateAPIView):
    """Create a new Customer user."""
    serializer_class = UserSerializer


