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


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("id", 'title', 'slug', )


class SubjectSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Subject
        fields = ("id", "title", "level", "slug", "lessons")


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


class SubjectForLessonSerializer(serializers.ModelSerializer):
    level = LevelSerializer(many=False)

    class Meta:
        model = Subject
        fields = (
            "title",
            "slug",
            "id",
            "level",
        )


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectForLessonSerializer(many=False)

    class Meta:
        model = Lesson
        fields = ('title', 'slug', 'description', 'photo', 'subject',)
