"""
View for User API
"""
from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Creates a user API view"""
    serializer_class = UserSerializer
