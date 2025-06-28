from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class GoogleOAuthTests(APITestCase):

    def test_google_redirect_missing_code(self):
        """
        Should return 400 if 'code' param is missing.
        """
        url = reverse('google_auth_redirect')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Missing code')

    def test_google_redirect_with_invalid_code(self):
        """
        Should return 400 if invalid code is supplied.
        """
        url = reverse('google_auth_redirect')
        response = self.client.get(url, {'code': 'invalid_code'})
        # Expecting failure because 'invalid_code' can't be exchanged for a token
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
