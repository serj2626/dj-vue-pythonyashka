from django.contrib import admin

from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post)"""

    list_display = (
        "title",
        "created_at",
        "updated_at",
        "slug",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin View for Tag)"""

    list_display = (
        "title",
        "slug",
    )
    ordering = ("title",)
