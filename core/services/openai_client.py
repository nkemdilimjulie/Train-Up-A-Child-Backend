# core/services/openai_client.py
"""
Centralized OpenAI client configuration.

PURPOSE:
- Creates ONE reusable OpenAI client for the entire backend.
- Prevents repeating API key logic in multiple files.
- Makes it easy to change OpenAI settings in one place later.

IMPORTANT:
- This file does NOT send prompts.
- It only prepares a configured client.
"""

from openai import OpenAI
from django.conf import settings

# Create a single OpenAI client using the API key from Django settings
# This client will be imported and reused by other services
client = OpenAI(api_key=settings.OPENAI_API_KEY)
