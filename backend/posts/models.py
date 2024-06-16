from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from pytils.translit import slugify


class Tag(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Tag {self.title}"

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    content = CKEditor5Field(verbose_name="Полное описание", config_name="extends")
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Post {self.title}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
