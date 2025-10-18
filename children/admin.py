from django.contrib import admin
from .models import Child

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "class_name", "date_registered")
    search_fields = ("first_name", "last_name", "guardian_name")
