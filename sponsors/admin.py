from django.contrib import admin
from .models import SponsorProfile


@admin.register(SponsorProfile)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("id", "get_username", "get_first_name", "get_last_name", "get_email", "organization_name")
    search_fields = ("user__username", "user__first_name", "user__last_name", "organization_name")

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = "Username"

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = "First Name"

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = "Last Name"

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = "Email"

