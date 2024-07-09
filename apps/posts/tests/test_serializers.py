from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.profiles.models import Profile

from ..models import Comment, Post
from ..serializers import CommentSerializer, PostSerializer

User = get_user_model()


class PostSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user)
        self.post = Post.objects.create(
            title="Post Title",
            content="Post Content",
            author=self.profile,
        )

    def test_post_serializer(self):
        serializer = PostSerializer(self.post)
        data = serializer.data
        self.assertEqual(data["title"], "Post Title")
        self.assertEqual(data["content"], "Post Content")
        self.assertEqual(data["author"], self.profile.id)


class CommentSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user)
        self.post = Post.objects.create(
            title="Post Title",
            content="Post Content",
            author=self.profile,
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.profile,
            content="Comment Content",
        )

    def test_comment_serializer(self):
        serializer = CommentSerializer(self.comment)
        data = serializer.data
        self.assertEqual(data["content"], "Comment Content")
        self.assertEqual(data["author"], self.profile.id)
        self.assertEqual(data["post"], self.post.id)
