from rest_framework import generics, mixins
from rest_framework.response import Response

from .models import Lesson, Level, Subject
from .serializers import (
    LessonSerializer,
    LevelDetailSerializer,
    LevelSerializer,
    SubjectSerializer,
)


class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelDetailView(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelDetailSerializer
    lookup_field = "slug"


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = "slug"


class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = "slug"
