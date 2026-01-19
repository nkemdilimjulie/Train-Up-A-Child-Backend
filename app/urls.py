# app/urls.py
from django.urls import path
from .views import translate_faq

urlpatterns = [
    path("api/translate-faq/", translate_faq, name="translate_faq"),
]
