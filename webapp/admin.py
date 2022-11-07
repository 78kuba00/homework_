from django.contrib import admin
from webapp.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'details', 'deadline']
    list_filter = ['status']
    search_fields = ['title']
    delete_confirmation_template = ['id', 'title', 'status', 'details']
    exclude = []

admin.site.register(Task, TaskAdmin)