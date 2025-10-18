from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("id", "sponsor", "amount", "date", "stripe_session_id")
    list_filter = ("date",)
    search_fields = ("sponsor__user__username", "stripe_session_id")

