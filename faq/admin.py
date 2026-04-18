# faq/admin.py
from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("slug",)
    prepopulated_fields = {"slug": ("question",)}
