# donations/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import stripe
from .models import Donation
from .serializers import DonationSerializer
from sponsors.models import SponsorProfile

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(["POST"])
@permission_classes([AllowAny])
def create_checkout_session(request):
    """
    Creates a Stripe checkout session for donation and attaches it to the sponsor profile.
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

        # Attach to sponsor profile if user is authenticated
        sponsor_profile = None
        if request.user.is_authenticated:
            try:
                sponsor_profile = SponsorProfile.objects.get(user=request.user)
            except SponsorProfile.DoesNotExist:
                sponsor_profile = None

        # Save donation record
        Donation.objects.create(
            user=request.user if request.user.is_authenticated else None,
            sponsor=sponsor_profile,
            amount=amount,
            stripe_payment_intent=checkout_session.payment_intent
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
