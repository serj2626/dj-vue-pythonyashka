from django.contrib import admin
from .models import Subject, Level, Lesson


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    '''Admin View for Subject)'''

    list_display = ('title', 'level', 'slug', )
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    '''Admin View for Level)'''

    list_display = ('title','level_number', 'slug', )
    list_editable = ('level_number', )

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    '''Admin View for Lesson)'''

    list_display = ('title', 'slug',  'subject', )
