# donations/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.db import transaction
import stripe
from .models import Donation
from .serializers import DonationSerializer
from sponsors.models import SponsorProfile

stripe.api_key = settings.STRIPE_SECRET_KEY


# -------------------------------------------
# 1️⃣ Anonymous / Fast Donation (no login)
# -------------------------------------------
@api_view(["POST"])
@permission_classes([AllowAny])
def create_checkout_session(request):
    """
    Anonymous donation - anyone can donate without logging in.
    """
    try:
        amount = request.data.get("amount")
        if not amount:
            return Response({"error": "Amount is required"}, status=status.HTTP_400_BAD_REQUEST)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "Fast Donation"},
                    "unit_amount": int(float(amount) * 100),
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="http://localhost:3000/donate/success",
            cancel_url="http://localhost:3000/donate/cancel",
        )

        # Save donation without linking to user/sponsor
        Donation.objects.create(
            amount=amount,
            stripe_payment_intent=checkout_session.payment_intent
        )

        return Response({"url": checkout_session.url})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# -------------------------------------------
# 2️⃣ Sponsor Donation (requires login)
# -------------------------------------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_sponsor_checkout_session(request):
    """
    Logged-in sponsor donation - linked to sponsor profile.
    """
    amount = request.data.get("amount")
    if not amount:
        return Response({"error": "Amount is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        sponsor_profile = SponsorProfile.objects.filter(user=request.user).first()
        if not sponsor_profile:
            return Response({"error": "Sponsor profile not found for this user."}, status=status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": "Sponsor Donation"},
                        "unit_amount": int(float(amount) * 100),
                    },
                    "quantity": 1,
                }],
                mode="payment",
                success_url="http://localhost:3000/donate/success",
                cancel_url="http://localhost:3000/donate/cancel",
            )

            Donation.objects.create(
                user=request.user,
                sponsor=sponsor_profile,
                amount=amount,
                stripe_payment_intent=checkout_session.payment_intent,
            )

        return Response({"url": checkout_session.url})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_donations_by_user(request, username):
    """
    Return all donations made by a given user (username).
    """
    donations = Donation.objects.filter(user__username=username).order_by("-created_at")
    serializer = DonationSerializer(donations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
