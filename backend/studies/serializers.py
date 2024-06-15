from rest_framework import serializers

from .models import Level, Subject, Lesson


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ("title", "slug", 'id', )


class LevelDetailWithSubjectsSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = ("title", "slug", 'id', "subjects", )

    def get_subjects(self, obj):
        return SubjectSerializer(obj.subjects.all(), many=True).data


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("title", "level", "slug")


# class LessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = ('title', 'slug', 'description', 'photo', 'subject', )
