from django.urls import path

from .views import PostDetailView, TagDetailView, TagListView

urlpatterns = [
    
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<slug:slug>/", TagDetailView.as_view(), name="tag-detail"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
]
