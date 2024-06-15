from .serializers import LevelSerializer
from .models import Level, Subject, Lesson
from rest_framework import generics, mixins
from rest_framework.response import Response


class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelDetailView(generics.RetrieveAPIView):
    queryset = Level.objects.all()


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = LevelSerializer