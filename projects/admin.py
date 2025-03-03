from django.contrib import admin
from .models import Project, Submission

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'assigned_class', 'due_date', 'created_at')
    list_filter = ('created_by', 'assigned_class', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('project', 'student', 'status', 'submitted_at', 'score')
    list_filter = ('status', 'submitted_at', 'project')
    search_fields = ('project__title', 'student__username', 'comments', 'feedback')
    date_hierarchy = 'submitted_at'
