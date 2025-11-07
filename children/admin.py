from django.contrib import admin
from .models import ChildProfile
from django.utils.html import format_html

@admin.register(ChildProfile)
class ChildAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "get_first_name",
        "get_last_name",
        "get_email",
        "age",
        "class_name",
        "guardian_name",
        "date_registered",
    )
    search_fields = ("user__username", "guardian_name", "user__first_name", "user__last_name", "user__email")

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = "First Name"

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = "Last Name"

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = "Email"

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.photo.url)
        return "-"
    photo_preview.short_description = "Photo"
    