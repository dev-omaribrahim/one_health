from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Profile
from ..serializers import ProfileSerializer

User = get_user_model()


class ProfileSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, bio="This is a test bio")
        self.serializer = ProfileSerializer(instance=self.profile)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ["id", "user", "bio", "profile_picture"])

    def test_user_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["user"], self.user.id)

    def test_bio_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["bio"], self.profile.bio)
