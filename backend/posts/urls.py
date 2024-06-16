from django.urls import path

from .views import PostDetailView, TagDetailView, TagListView

urlpatterns = [
    path("<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<slug:slug>/", TagDetailView.as_view(), name="tag-detailt"),
]
