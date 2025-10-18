from django.contrib import admin
from .models import User as Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """for easy data inspection in admin panel"""
    list_display = ("id", "username", "email", "is_sponsor", "is_guest")
    search_fields = ("username", "email")

