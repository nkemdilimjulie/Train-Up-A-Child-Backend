# faq/models.py
from django.db import models

class FAQ(models.Model):
    slug = models.SlugField(unique=True)
    question = models.TextField()
    answer = models.TextField()
    is_public = models.BooleanField(default=True)

    # future translations
    question_de = models.TextField(blank=True, null=True)
    answer_de = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.slug
