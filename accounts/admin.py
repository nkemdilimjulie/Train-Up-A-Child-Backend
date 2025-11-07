from django.contrib import admin
from .models import User as Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """for easy data inspection in admin panel"""
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_sponsor", "is_guest", "is_child")
    list_display = ("username", "first_name", "last_name", "email", "is_sponsor", "is_guest", "is_child")

