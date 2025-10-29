from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def send_email(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        if not all([name, email, message]):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        send_mail(
            subject=f"New Message from {name}",
            message=f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email="fullstackcode0707@gmail.com",  # your app email
            recipient_list=["amonline0707@yahoo.com"],  # or your preferred inbox
        )

        return Response({"success": True}, status=status.HTTP_200_OK)
    except Exception as e:
        print("Email send error:", e)
        return Response({"error": "Failed to send message."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

