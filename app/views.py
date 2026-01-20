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

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from app.models import FAQ
from app.services.faq_translation_service import get_or_create_faq_translation


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def translate_faq(request):
    """
    Translate an existing FAQ into a selected language.

    Expected payload:
    {
        "faq_id": 1,
        "language": "de"
    }
    """

    faq_id = request.data.get("faq_id")
    language = request.data.get("language", "de")

    if not faq_id:
        return Response(
            {"error": "faq_id is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        faq = FAQ.objects.get(id=faq_id)
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
                "faq_id": faq.id,
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
