from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'full_name',
        'course',
        'year_level',
        'section',
    )

    search_fields = (
        'student_id',
        'full_name',
        'course',
        'section',
    )