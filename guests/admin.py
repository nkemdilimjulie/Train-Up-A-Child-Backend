from django.contrib import admin
from .models import GuestProfile

@admin.register(GuestProfile)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "first_name", "last_name", "email")
    search_fields = ("user__username", "email")
