# core/services/openai_service.py
"""
Generic OpenAI text interaction service.

PURPOSE:
- Provides a simple helper function for asking OpenAI general questions.
- Intended for future features like:
  - Chat assistant
  - Help bot
  - AI-generated explanations (non-authoritative)

IMPORTANT:
- This does NOT touch FAQs.
- This does NOT store anything in the database.
- Output is NOT considered "official content".
"""

from core.services.openai_client import client

# System message that defines how the assistant should behave
SYSTEM_PROMPT = (
    "You are a helpful assistant for the Train-Up-A-Child platform. "
    "Be concise, respectful, and supportive."
)

def ask_openai(prompt: str) -> str:
    """
    Sends a free-form user prompt to OpenAI and returns the AI response.

    USE CASES (later):
    - Chat-style assistant
    - Help questions
    - Draft suggestions (not authoritative)

    NOT FOR:
    - Translations stored in DB
    - Official FAQ answers
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
        max_tokens=300,
    )

    return response.choices[0].message.content.strip()
