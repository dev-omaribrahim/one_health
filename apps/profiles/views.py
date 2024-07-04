from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]

