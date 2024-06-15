from django.urls import path
from .views import LevelListView, LevelDetailView, SubjectDetailView, LessonDetailView

urlpatterns = [
    path('levels/', LevelListView.as_view(), name='level-list'),
    path('levels/<slug:slug>/', LevelDetailView.as_view(), name='level-detail'),
    path('subjects/<slug:slug>/', SubjectDetailView.as_view(), name='subject-detail'),
    path('lessons/<slug:slug>/', LessonDetailView.as_view(), name='lesson-detail'),
]
