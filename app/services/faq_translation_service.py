from app.models import FAQ, FAQTranslation
from app.services.translation import translate_faq_with_openai


def get_or_create_faq_translation(
    faq: FAQ,
    language_code: str,
):
    """
    Returns a translated FAQ.
    - Uses DB if translation already exists
    - Otherwise calls OpenAI, saves result, then returns it
    """

    # 1️⃣ Check if translation already exists
    existing = FAQTranslation.objects.filter(
        faq=faq,
        language_code=language_code
    ).first()

    if existing:
        return existing

    # 2️⃣ Translate using OpenAI
    translated_q, translated_a = translate_faq_with_openai(
        question=faq.question,
        answer=faq.answer,
        target_lang=language_code,
    )

    # 3️⃣ Save translation
    translation = FAQTranslation.objects.create(
        faq=faq,
        language_code=language_code,
        question_translated=translated_q,
        answer_translated=translated_a,
    )

    return translation
