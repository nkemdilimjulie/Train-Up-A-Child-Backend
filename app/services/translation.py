# app/services/translation.py
"""
AI-powered FAQ translation service.

PURPOSE:
- Takes YOUR EXISTING FAQ content (question + answer).
- Uses OpenAI ONLY to translate it.
- Preserves meaning, tone, and child-friendliness.
- NEVER invents new content.

IMPORTANT CONCEPT:
- Your FAQ content is the SOURCE OF TRUTH.
- AI is a translation TOOL, not a content creator.
"""

import time
from typing import Tuple
from django.conf import settings
from core.services.openai_client import client

# System instruction that strictly defines translation behavior
SYSTEM_PROMPT = (
    "You are a professional translator. "
    "Translate the provided question and answer into the requested language. "
    "Maintain the meaning and tone, keep the translation child-friendly (suitable for ages 4-12), "
    "avoid idioms that don't translate well, and preserve important names like TRAUCCO and TRUACCO. "
    "Return JSON with keys: question and answer."
)

def build_translation_prompt(question: str, answer: str, target_lang: str) -> str:
    """
    Builds a structured translation prompt for OpenAI.

    WHY:
    - Clear formatting improves translation quality.
    - JSON output makes parsing reliable.
    """

    return (
        f"Translate the following into {target_lang} and output JSON with keys 'question' and 'answer'.\n\n"
        f"QUESTION:\n{question}\n\n"
        f"ANSWER:\n{answer}\n\n"
        "Ensure the answer is simple and child-appropriate. Do not add extra commentary."
    )

def translate_faq_with_openai(
    question: str,
    answer: str,
    target_lang: str,
    max_retries: int = 2
) -> Tuple[str, str]:
    """
    Translates a single FAQ (question + answer) into the target language.

    INPUT:
    - question: original FAQ question (your content)
    - answer: original FAQ answer (your content)
    - target_lang: e.g. 'German', 'French'

    OUTPUT:
    - (translated_question, translated_answer)

    RETRY LOGIC:
    - Retries automatically if OpenAI fails temporarily.
    """

    prompt = build_translation_prompt(question, answer, target_lang)

    for attempt in range(max_retries + 1):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,  # deterministic translation
                max_tokens=600,
            )

            content = response.choices[0].message.content.strip()


            # Expect JSON output from OpenAI
            import json
            parsed = json.loads(content)

            q_trans = parsed.get("question", "").strip()
            a_trans = parsed.get("answer", "").strip()

            if not q_trans or not a_trans:
                raise ValueError("Translation missing required fields")

            return q_trans, a_trans

        except Exception:
            if attempt < max_retries:
                time.sleep(1 + attempt * 2)
                continue
            raise
