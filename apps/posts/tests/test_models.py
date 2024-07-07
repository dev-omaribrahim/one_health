from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.profiles.models import Profile
from apps.categories.models import Category
from apps.tags.models import Tag
from ..models import Post, Comment

User = get_user_model()

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user)
        self.category = Category.objects.create(name='Category1')
        self.tag = Tag.objects.create(name='Tag1')
        self.post = Post.objects.create(
            title='Post Title',
            content='Post Content',
            author=self.profile,
        )
        self.post.categories.add(self.category)
        self.post.tags.add(self.tag)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Post Title')
        self.assertEqual(self.post.content, 'Post Content')
        self.assertEqual(self.post.author, self.profile)
        self.assertIn(self.category, self.post.categories.all())
        self.assertIn(self.tag, self.post.tags.all())

    def test_post_string_representation(self):
        self.assertEqual(str(self.post), 'Post Title')


class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user)
        self.post = Post.objects.create(
            title='Post Title',
            content='Post Content',
            author=self.profile,
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.profile,
            content='Comment Content',
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, 'Comment Content')
        self.assertEqual(self.comment.author, self.profile)
        self.assertEqual(self.comment.post, self.post)

    def test_comment_string_representation(self):
        self.assertEqual(str(self.comment), f'Comment by {self.user.username} on {self.post.title}')
