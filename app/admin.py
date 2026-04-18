# app/admin.py
# Register your models here.

from django.contrib import admin, messages
from app.models import FAQ, FAQTranslation
from app.services.faq_translation_service import get_or_create_faq_translation

# admin.site.register(FAQ)
# admin.site.register(FAQTranslation)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Admin configuration for FAQs.

    Adds a custom action that allows staff users to translate
    selected FAQs into predefined languages using OpenAI.
    """

    list_display = ("id", "slug", "created_at")
    search_fields = ("slug", "question")
    actions = ["translate_selected_faqs"]

    def translate_selected_faqs(self, request, queryset):
        """
        Admin action:
        Translates selected FAQs into supported languages
        and saves results into FAQTranslation table.
        """

        supported_languages = ["de", "fr"]  # you can expand later
        created_count = 0

        for faq in queryset:
            for lang in supported_languages:
                translation = get_or_create_faq_translation(
                    faq=faq,
                    language_code=lang
                )
                if translation:
                    created_count += 1

        self.message_user(
            request,
            f"Translation completed. {created_count} translations created or reused.",
            level=messages.SUCCESS,
        )

    translate_selected_faqs.short_description = "Translate selected FAQs"


@admin.register(FAQTranslation)
class FAQTranslationAdmin(admin.ModelAdmin):
    """
    Admin view for translated FAQs.
    """

    list_display = ("faq", "language_code", "translated_at")
    list_filter = ("language_code",)
    search_fields = ("faq__question",)
