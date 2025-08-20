from rest_framework.response import Response
from rest_framework.views import APIView

class APIDocumentationView(APIView):
    def get(self, request):
        return Response({
            "message": "Welcome to Train-Up-A-Child API",
            "endpoints": {
                "sponsors": "/api/sponsors/",
                "children": "/api/children/",
                "donations": "/api/donate/",
                "users": "/api/users/",
            }
        })

