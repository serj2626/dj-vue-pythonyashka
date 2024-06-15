from django.urls import path
from .views import LevelListView

urlpatterns = [
    path('levels/', LevelListView.as_view(), name='level-list'),
]
