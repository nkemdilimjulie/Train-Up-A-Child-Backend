# donations/webhook.py
import stripe
from decimal import Decimal
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Donation
from sponsors.models import SponsorProfile
from django.contrib.auth import get_user_model

User = get_user_model()
stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

    try:
        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]

            payment_intent = session.get("payment_intent")
            amount_total = session.get("amount_total")

            if not payment_intent or amount_total is None:
                return JsonResponse({"error": "Invalid session data"}, status=400)

            # ✅ Convert safely
            amount = Decimal(amount_total) / 100

            metadata = session.get("metadata") or {}

            user_id = metadata.get("user_id")
            sponsor_id = metadata.get("sponsor_id")

            user = None
            sponsor = None

            if user_id:
                user = User.objects.filter(id=user_id).first()

            if sponsor_id:
                sponsor = SponsorProfile.objects.filter(id=sponsor_id).first()

            # ✅ Prevent duplicates
            if not Donation.objects.filter(
                stripe_payment_intent=payment_intent
            ).exists():

                Donation.objects.create(
                    user=user,
                    sponsor=sponsor,
                    amount=amount,
                    stripe_payment_intent=payment_intent,
                )

    except Exception as e:
        print("🔥 WEBHOOK ERROR:", str(e))
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"status": "success"})