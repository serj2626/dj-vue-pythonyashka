from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from pytils.translit import slugify

# level 1 - Start in Python
# level 2 - OOP
# level 3 - Algorithms and Data Structures
# level 4 - Frameworks
# level 5 - Async


def get_path_for_photos(instance, filename):
    return f"studies/lessons/{instance.slug}/{filename}"


class Level(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    level_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"
        ordering = ["level_number"]


class Subject(models.Model):
    title = models.CharField(max_length=355, verbose_name="Тема", unique=True)
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, related_name="subjects", verbose_name="Уровень"
    )
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Lesson(models.Model):
    title = models.CharField(max_length=355, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True)
    description = CKEditor5Field(verbose_name="Полное описание", config_name="extends")
    photo = models.ImageField(
        upload_to=get_path_for_photos, verbose_name="Фото", blank=True
    )
    subject = models.ForeignKey(
        Subject, related_name="lessons", on_delete=models.CASCADE, verbose_name="Тема"
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
