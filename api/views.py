import requests

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponseNotFound
from django.shortcuts import redirect
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

        return Response(response.json(), status=response.status_code)  # Should be redirect to verification success page


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

def index(request):
    return redirect("https://dsfs2-uyaaa-aaaam-qbgpq-cai.icp0.io/")

class GoogleLogin(SocialLoginView):
    """
    Navigate to the url below, sign in with google, get credentials
    https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=https://dsfs2-uyaaa-aaaam-qbgpq-cai.icp0.io/google/callback&prompt=consent&response_type=code&client_id=<YOUR CLIENT ID>&scope=openid%20email%20profile&access_type=offline
    Credentials are then POSTed to this endpoint then user gets authenticated
    """

    adapter_class = GoogleOAuth2Adapter
    callback_url = "https://dsfs2-uyaaa-aaaam-qbgpq-cai.icp0.io/google/callback"
    client_class = OAuth2Client