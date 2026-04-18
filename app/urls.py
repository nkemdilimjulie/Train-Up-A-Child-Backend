# app/urls.py
from django.urls import path
from .views import translate_faq, list_faqs

urlpatterns = [
    path("api/translate-faq/", translate_faq, name="translate_faq"),
    path("api/faqs/", list_faqs, name="list_faqs"),
]
