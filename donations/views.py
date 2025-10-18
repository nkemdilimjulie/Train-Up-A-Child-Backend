
import stripe
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from sponsors.models import SponsorProfile
from .models import Donation

from rest_framework import viewsets, permissions
from .models import Donation
from .serializers import DonationSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY  # set in settings/env

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all().order_by("-date")
    serializer_class = DonationSerializer
    permission_classes = [permissions.AllowAny]


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_checkout_session(request):
    """
    Expects: { sponsor_id, amount }
    Creates a Donation record (pending) then creates stripe checkout session and returns session.id
    """
    sponsor_id = request.data.get("sponsor_id")
    amount = request.data.get("amount")
    try:
        sponsor = SponsorProfile.objects.get(id=sponsor_id)
    except SponsorProfile.DoesNotExist:
        return Response({"error":"Sponsor not found"}, status=status.HTTP_404_NOT_FOUND)
    if not amount:
        return Response({"error":"Amount required"}, status=status.HTTP_400_BAD_REQUEST)
    # Create pending donation
    donation = Donation.objects.create(sponsor=sponsor, amount=amount)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(float(amount) * 100),
                    "product_data": {"name": f"Donation by {sponsor.user.username}"}
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url=settings.STRIPE_SUCCESS_URL + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=settings.STRIPE_CANCEL_URL,
            metadata={"donation_id": donation.id, "sponsor_id": sponsor.id},
        )
        donation.stripe_session_id = session.id
        donation.save()
        return Response({"id": session.id})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def stripe_webhook(request):
    """Handles Stripe webhook events - confirms successful payments and marks donations as completed."""
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET  # add this to your .env

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    # Handle successful payment
    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        sponsor_id = payment_intent.get("metadata", {}).get("sponsor_id")
        amount = payment_intent["amount_received"] / 100  # cents to €
        Donation.objects.create(
            sponsor_id=sponsor_id,
            amount=amount,
            status="completed"
        )

    return HttpResponse(status=200)