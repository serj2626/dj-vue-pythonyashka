from rest_framework import serializers

from .models import Post, Tag


class PostForTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "slug")


class TagDetailSerializer(serializers.ModelSerializer):
    posts = PostForTagSerializer(many=True)

    class Meta:
        model = Tag
        fields = ("title", "slug", "posts")


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            "id",
            "title",
            "slug",
        )


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "slug", "created_at", "tags")
