import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import CustomLoginSerializer
from django.conf import settings

from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from urllib.parse import urlencode
from django.contrib.auth import get_user_model
import logging
from requests import request
logger = logging.getLogger(__name__)
User = get_user_model()

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CustomLoginView(generics.GenericAPIView):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        # Enforce max 2 sessions (refresh tokens)
        tokens = OutstandingToken.objects.filter(user=user).order_by('created_at')
        if tokens.count() >= 2:
            # Remove oldest token
            oldest_token = tokens.first()
            oldest_token.delete()

        # Issue new tokens
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response({
            'refresh': str(refresh),
            'access': str(access),
            'user':{
                'email': user.email,
                'username': user.username,
                'isAdmin':user.is_staff
            }
        }, status=status.HTTP_200_OK)

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "email": user.email,
            "username": user.username,
        })
    




class GoogleAuthRedirectAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        code = request.query_params.get('code')
        state = request.query_params.get('state')

        if not code:
            return Response({'detail': 'Missing code'}, status=400)

        token_url = 'https://oauth2.googleapis.com/token'
        token_data = {
            'code': code,
            'client_id': settings.SOCIAL_AUTH_GOOGLE_CLIENT_ID,
            'client_secret': settings.SOCIAL_AUTH_GOOGLE_SECRET,
            'redirect_uri': 'http://localhost:8000/auth/account/google/login/callback/',
            'grant_type': 'authorization_code'
        }

        token_response = requests.post(token_url, data=token_data)
        if token_response.status_code != 200:
            print(f"[DEBUG] Failed to exchange code for token. Response: {token_response.text}")
            return Response({'detail': 'Failed to fetch access token'}, status=400)

        token_json = token_response.json()
        access_token = token_json.get('access_token')
        print(f"[DEBUG] Google access_token: {access_token}")

        if not access_token:
            return Response({'detail': 'No access token received'}, status=400)

        # Fetch user info
        user_info_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        user_info_params = {'access_token': access_token}
        user_info_response = requests.get(user_info_url, params=user_info_params)
        if user_info_response.status_code != 200:
            print(f"[DEBUG] Failed to fetch user info. Response: {user_info_response.text}")
            return Response({'detail': 'Failed to fetch user info'}, status=400)

        user_info = user_info_response.json()
        print(f"[DEBUG] User info received: {user_info}")

        email = user_info.get('email')
        if not email:
            return Response({'detail': 'Email not found in user info'}, status=400)

        # Get or create user
        user, created = User.objects.get_or_create(
            email=email,
            defaults={'username': email.split('@')[0]}
        )

        print(f"[DEBUG] User {'created' if created else 'found'}: {user}")

        #max 2 tokens
        tokens = OutstandingToken.objects.filter(user=user).order_by('created_at')
        if tokens.count() >= 2:
            # Remove oldest token
            oldest_token = tokens.first()
            oldest_token.delete()
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        print(f"[DEBUG] Tokens generated for user {user.id}")

         
        params = {
            'access': str(access),
            'refresh': str(refresh),
            'username': user.username,
            'email': user.email,
        }
        frontend_url = settings.FRONTEND_URL  # e.g. 'http://localhost:5173/auth/social/google/callback'
        redirect_url = f"{frontend_url}auth/google/callback?{urlencode(params)}"
        return redirect(redirect_url)
