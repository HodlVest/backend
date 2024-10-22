import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponseNotFound
from django.conf import settings

class VerifyEmail(APIView):
    """
    View accessed from URL send to the email
    Verifies user email from token sent to mail
    Email is then verified successfully :)
    Redirects to frontend verification success page
    """

    def get(self, request, *args, **kwargs):
        key = kwargs.get("key", None)
        
        if settings.DEBUG:
            email_verify_url = "http://127.0.0.1:8000/api/auth/registration/verify-email/"
        else:
            email_verify_url = f"https://hodlvest.onrender.com/api/auth/registration/verify-email/"
        
        response = requests.post(email_verify_url, json={
            "key": key,
        })

        return Response(response.json(), status=response.status_code)  # Should be redirect


class NotFoundView(APIView):
    def get(self, request):
        return HttpResponseNotFound()


class PasswordReset(APIView):
    """
    Password Reset
    Sends user credentials required to reset password to Frontend
    Credentials are used to reset password on the /confirm endpoint via POST
    New password + confirm is POSTed alone with given credentials
    """

    def get(self, request, *args, **kwargs):
        uid64 = kwargs.get('uid64', None)
        token = kwargs.get('token', None)
        
        return Response({
            'uib64': uid64,
            'token': token
        }, status=status.HTTP_200_OK)  # should be redirect