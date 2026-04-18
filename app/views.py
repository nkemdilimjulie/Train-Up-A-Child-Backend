# app/views.py

"""
API endpoint for translating an FAQ via OpenAI.

FLOW:
Frontend → Backend → Database → OpenAI (if needed) → Database → Frontend

NOTE:
- Uses stored FAQs
- Saves translations automatically
- Avoids repeated OpenAI calls
"""
from httpx import request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from app.models import FAQ, FAQTranslation
from app.services.faq_translation_service import get_or_create_faq_translation
from rest_framework.permissions import AllowAny

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def translate_faq(request):
    """
    Translate an existing FAQ into a selected language.

    # Expected payload:
    # {
    #     "faq_slug": "what-is-train-up-a-child",
    #     "language": "de"
    # }
    """

    faq_slug = (request.data.get("faq_slug") or "").strip()
    language = (request.data.get("language") or "German").strip()


    if not faq_slug:
        return Response(
            {"error": "faq_slug is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        faq = FAQ.objects.get(slug=faq_slug)
    except FAQ.DoesNotExist:
        
        return Response(
            {"error": "FAQ not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        translation = get_or_create_faq_translation(
            faq=faq,
            language_code=language
        )

        return Response(
            {
                "faq_slug": faq.slug,
                "language": translation.language_code,
                "question": translation.question_translated,
                "answer": translation.answer_translated,
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response(
            {
                "error": "Translation failed.",
                "details": str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["GET"])
@permission_classes([AllowAny])
def list_faqs(request):
    """
    Return FAQs in the requested language.

    Query param:
    ?lang=de   (default: en)

    Behavior:
    - If translation exists → return translated text
    - Else → fallback to original English
    """

    lang = request.GET.get("lang", "en")
    faqs = FAQ.objects.all().order_by("created_at")

    response_data = []

    for faq in faqs:
        translated = None

        if lang != "en":
            translated = FAQTranslation.objects.filter(
                faq=faq,
                language_code=lang
            ).first()

        response_data.append({
            "slug": faq.slug,
            "question": translated.question_translated if translated else faq.question,
            "answer": translated.answer_translated if translated else faq.answer,
            "language": lang if translated else "en",
        })

    return Response(response_data)
