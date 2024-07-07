from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.profiles.models import Profile
from apps.categories.models import Category
from apps.tags.models import Tag
from ..models import Post, Comment
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class PostViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user)
        self.client = APIClient()
        
        # Get JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        self.category = Category.objects.create(name='Category1')
        self.tag = Tag.objects.create(name='Tag1')

        self.post = Post.objects.create(
            title='Post Title',
            content='Post Content',
            author=self.profile,
        )
        self.post.categories.add(self.category)
        self.post.tags.add(self.tag)

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.profile,
            content='Comment Content',
        )

    def test_create_post(self):
        url = reverse('posts:post_list_create')
        data = {
            'title': 'New Post',
            'content': 'New Content',
            'author': self.profile.id,
            'categories': [self.category.id],
            'tags': [self.tag.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_retrieve_post(self):
        url = reverse('posts:post_detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_update_post(self):
        url = reverse('posts:post_detail', kwargs={'pk': self.post.pk})
        data = {'title': 'Updated Title'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_delete_post(self):
        url = reverse('posts:post_detail', kwargs={'pk': self.post.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_comment(self):
        url = reverse('posts:comment_list_create', kwargs={'post_id': self.post.pk})
        data = {
            'content': 'New Comment',
            'author': self.profile.id,
            'post': self.post.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_retrieve_comment(self):
        url = reverse('posts:comment_detail', kwargs={'post_id': self.post.pk, 'pk': self.comment.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.comment.content)

    def test_update_comment(self):
        url = reverse('posts:comment_detail', kwargs={'post_id': self.post.pk, 'pk': self.comment.pk})
        data = {'content': 'Updated Content'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated Content')

    def test_delete_comment(self):
        url = reverse('posts:comment_detail', kwargs={'post_id': self.post.pk, 'pk': self.comment.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
