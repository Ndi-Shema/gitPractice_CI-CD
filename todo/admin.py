from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'completed', 'start_time', 'end_time', 'owner')
    list_filter = ('completed', 'category', 'owner')
    search_fields = ('title', 'category', 'owner__username')
