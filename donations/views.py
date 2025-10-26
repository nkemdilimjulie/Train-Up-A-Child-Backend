
# donations/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import stripe
from .models import Donation
from .serializers import DonationSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(["POST"])
@permission_classes([AllowAny])
def create_checkout_session(request):
    """
    Creates a Stripe checkout session for donation.
    """
    try:
        amount = request.data.get("amount")
        if not amount:
            return Response({"error": "Amount is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Stripe requires amount in cents
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "Donation"},
                    "unit_amount": int(float(amount) * 100),
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="http://localhost:3000/donate/success",
            cancel_url="http://localhost:3000/donate/cancel",
        )

        # Optionally, save the donation record (without payment_intent yet)
        Donation.objects.create(
            amount=amount,
            stripe_payment_intent=checkout_session.payment_intent
        )

        return Response({"url": checkout_session.url})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
