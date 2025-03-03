from django.contrib import admin
from .models import Class

# Register your models here.

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'created_at')
    list_filter = ('teacher', 'created_at')
    search_fields = ('name', 'description', 'teacher__username')
    filter_horizontal = ('students',)
    date_hierarchy = 'created_at'
