# app/views.py

"""
API endpoint for translating an FAQ via OpenAI.

FLOW:
Frontend → Backend → OpenAI → Backend → Frontend

NOTE:
- Does NOT save translations yet
- Only returns translated text
"""

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from app.services.translation import translate_faq_with_openai


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def translate_faq(request):
    """
    Translate an FAQ question + answer into a selected language.

    Expected payload:
    {
        "question": "...",
        "answer": "...",
        "language": "German"
    }
    """
    question = request.data.get("question")
    answer = request.data.get("answer")
    language = request.data.get("language", "German")

    if not question or not answer:
        return Response(
            {"error": "Both question and answer are required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        translated_q, translated_a = translate_faq_with_openai(
            question=question,
            answer=answer,
            target_lang=language
        )

        return Response({
            "question": translated_q,
            "answer": translated_a
        })

    except Exception as e:
        return Response(
            {"error": "Translation failed", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
