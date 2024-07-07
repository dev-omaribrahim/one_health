from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.users_auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from ..models import Tag


class TagsAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.access_token = self.get_access_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def get_access_token(self, user):
        token = AccessToken.for_user(user)
        return str(token)

    def test_list_create_tags(self):
        url = reverse('tags:tag_list_create')
        data = {'name': 'Test Tag'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Check if tag was created and listed correctly

    def test_retrieve_update_delete_tag(self):
        tag = Tag.objects.create(name='Test Tag')
        url = reverse('tags:tag_detail', kwargs={'pk': tag.pk})
        updated_data = {'name': 'Updated Tag Name'}

        # Retrieve tag
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update tag
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tag.refresh_from_db()
        self.assertEqual(tag.name, 'Updated Tag Name')

        # Delete tag
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_access(self):
        # Test unauthorized access (without JWT token)
        self.client.credentials()  # Clear credentials
        url = reverse('tags:tag_list_create')
        data = {'name': 'Unauthorized Tag'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# Add more tests as needed for edge cases, permissions, etc.

