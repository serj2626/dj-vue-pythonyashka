# Generated by Django 5.0.6 on 2024-06-15 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_tag_post_slug_alter_post_title_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="title",
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
