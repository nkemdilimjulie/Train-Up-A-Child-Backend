from django.contrib import admin
from .models import SponsorProfile

@admin.register(SponsorProfile)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "organization", "phone", "address", "country", "joined_date")
    search_fields = ("user__username", "organization")
