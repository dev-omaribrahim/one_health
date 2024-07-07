from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuthTests(APITestCase):

    def setUp(self):
        self.register_url = reverse('users_auth:register')
        self.login_url = reverse('users_auth:token_obtain_pair')
        self.refresh_url = reverse('users_auth:token_refresh')
        self.logout_url = reverse('users_auth:logout')

        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'password_confirm': 'password123',
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_user_registration_password_mismatch(self):
        user_data = self.user_data.copy()
        user_data['password_confirm'] = 'differentpassword'
        response = self.client.post(self.register_url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_user_login(self):
        self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.login_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password'],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'invaliduser',
            'password': 'invalidpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_refresh(self):
        self.client.post(self.register_url, self.user_data)
        login_response = self.client.post(self.login_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password'],
        })
        refresh_token = login_response.data['refresh']
        response = self.client.post(self.refresh_url, {'refresh': refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_logout(self):
        # Register the user
        self.client.post(self.register_url, self.user_data)
        
        # Log in to get the access and refresh tokens
        login_response = self.client.post(self.login_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password'],
        })
        
        access_token = login_response.data['access']
        refresh_token = login_response.data['refresh']
        
        # Set the authorization header with the access token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        
        # Log out using the refresh token
        response = self.client.post(self.logout_url, {'refresh': refresh_token})
        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_logout_with_invalid_token(self):
        self.client.post(self.register_url, self.user_data)
        login_response = self.client.post(self.login_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password'],
        })
        invalid_refresh_token = 'invalidtoken'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        response = self.client.post(self.logout_url, {'refresh': invalid_refresh_token})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
