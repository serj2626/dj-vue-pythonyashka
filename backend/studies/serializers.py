from rest_framework import serializers

from .models import Level, Subject, Lesson


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = (
            "title",
            "slug",
            "id",
        )


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "title",  "slug")


class LevelDetailSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Level
        fields = (
            "title",
            "slug",
            "id",
            "subjects",
        )


# class LessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = ('title', 'slug', 'description', 'photo', 'subject', )
