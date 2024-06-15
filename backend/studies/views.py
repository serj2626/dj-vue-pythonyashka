from .serializers import LevelSerializer, LevelDetailSerializer
from .models import Level, Subject, Lesson
from rest_framework import generics, mixins
from rest_framework.response import Response


class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelDetailView(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelDetailSerializer
    lookup_field = 'slug'
