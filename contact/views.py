# contact/views.py
import requests
from django.conf import settings
from django.core.mail import EmailMessage
from django_ratelimit.decorators import ratelimit
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny]) # ✅ allow public access
@ratelimit(key='ip', rate='5/m', block=True) # 🚀 limit to 5 requests per minute per IP to prevent abuse
def send_email(request):
    try:
        # 1. Get data from request
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')
        captcha_response = request.data.get('captcha_token')  # 👈 CAPTCHA token from frontend

        # 2. Validate required fields
        if not all([name, email, message, captcha_response]):
            return Response({"error": "All fields including captcha are required."}, status=status.HTTP_400_BAD_REQUEST)

        # 3. Verify CAPTCHA with Google
        verify = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                "secret": settings.RECAPTCHA_SECRET_KEY,  # 👈 
                "response": captcha_response
            }
        )

        result = verify.json()

        if not result.get("success"):
            return Response(
                {"error": "Captcha verification failed."},
                status=status.HTTP_400_BAD_REQUEST
            )


        # 4. Send email AFTER verification
        email_message = EmailMessage(
            subject=f"TRUACCO contact Message from {name}",
            body=f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email="trainupachild.project@gmail.com", #  app email
            to=["trainupachild.project@gmail.com"], # receiver email address: users messages are seen here
            reply_to=[email], # 👈replies directly to user/sender email when you click Reply from recipient email
        )

        email_message.send()

        # 5. Success response 
        return Response({"success": True}, status=status.HTTP_200_OK)
    except Exception as e:
        print("Email send error:", e)
        return Response({"error": "Failed to send message."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

