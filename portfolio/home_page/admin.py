from django.contrib import admin
from .models import Work, ProgrammingLanguage
from django.utils.html import format_html

from .models import Work, ProgrammingLanguage, Education, Skill


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'programming_language_image')

    def programming_language_image(self, obj):
        if obj.image:  # Check if image exists
            return format_html(
                '<img src="{}" alt="{}" width="35" height="35">',
                obj.image.url,  # Use obj.image.url for direct access
                obj.name
            )
        else:
            return 'No Image'  # Placeholder or empty string if no image

    programming_language_image.short_description = 'Image'


class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'work_images_image', 'programming_languages_name')

    def programming_languages_name(self, obj):
        return ', '.join(str(lang) for lang in obj.programming_languages.all())

    programming_languages_name.short_description = 'Programming Languages'

    def work_images_image(self, obj):
        if obj.work_images:  # Check if work_images field exists
            return format_html(
                '<img src="{}" alt="{}" width="20" height="20">',
                obj.work_images.url,  # Use obj.work_images.url for direct access
                obj.name
            )
        else:
            return 'No Image'  # Placeholder or empty string if no image

    work_images_image.short_description = 'Image'

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'program')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Customize list display fields
    
admin.site.register(Work, WorkAdmin)
admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skill, SkillAdmin)