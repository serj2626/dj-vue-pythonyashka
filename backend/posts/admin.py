from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post)'''

    list_display = ('title', 'created_at', 'updated_at', )
