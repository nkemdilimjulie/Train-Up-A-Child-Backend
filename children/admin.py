from django.contrib import admin
from .models import ChildProfile

@admin.register(ChildProfile)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "age", "class_name", "guardian_name", "date_registered")
    search_fields = ("user__username", "guardian_name")
