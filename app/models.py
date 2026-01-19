# app/models.py
from django.db import models

class FAQ(models.Model):
    """
    Primary FAQ content created by YOU.

    This is the SOURCE OF TRUTH.
    AI NEVER modifies these fields.
    """
    slug = models.SlugField(unique=True)          # e.g. "register-child"
    question = models.TextField()                 # source language (e.g. English)
    answer = models.TextField()                   # source answer (English)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FAQTranslation(models.Model):
    """
    Stores AI-generated translations of an FAQ.

    IMPORTANT:
    - Linked to original FAQ
    - Optional per language
    - Safe to regenerate
    """
    faq = models.ForeignKey(FAQ, related_name="translations", on_delete=models.CASCADE)
    language_code = models.CharField(max_length=10)    # e.g. "de", "fr", "yo"
    question_translated = models.TextField()
    answer_translated = models.TextField()
    translated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("faq", "language_code")
