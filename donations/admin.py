# donations/admin.py
from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "amount", "stripe_payment_intent", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "stripe_payment_intent")
    readonly_fields = ("stripe_payment_intent", "created_at")
