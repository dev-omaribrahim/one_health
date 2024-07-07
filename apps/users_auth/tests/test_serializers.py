# users_auth/tests/test_serializers.py

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from ..serializers import UserSerializer, MyTokenObtainPairSerializer

User = get_user_model()

class UserSerializerTests(APITestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'password_confirm': 'password123',
        }
        self.invalid_user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'password_confirm': 'differentpassword',
        }

    def test_user_serializer_valid_data(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))

    def test_user_serializer_invalid_data(self):
        serializer = UserSerializer(data=self.invalid_user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)

class MyTokenObtainPairSerializerTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )

    def test_token_obtain_pair_serializer(self):
        serializer = MyTokenObtainPairSerializer(data={
            'username': self.user.username,
            'password': 'password123'
        })
        self.assertTrue(serializer.is_valid())
        token = serializer.validated_data['access']
        refresh = serializer.validated_data['refresh']
        self.assertIsNotNone(token)
        self.assertIsNotNone(refresh)

        # Decode the token to check custom claims
        refresh_token = RefreshToken(refresh)
        self.assertEqual(refresh_token['username'], self.user.username)
