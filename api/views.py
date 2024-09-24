import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponseNotFound


class VerifyEmail(APIView):
    """
    View accessed from URL send to the email
    Verifies user email from token sent to mail
    Email is then verified successfully :)
    Redirects to frontend verification success page
    """

    def get(self, request, *args, **kwargs):
        key = kwargs.get("key", None)
        response = requests.post("http://127.0.0.1:8000/api/auth/registration/verify-email/", json={
            "key": key,
        })
        return Response(response.json(), status=response.status_code)

class NotFoundView(APIView):
    def get(self, request):
        return HttpResponseNotFound()