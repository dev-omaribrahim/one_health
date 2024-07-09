from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Profile

User = get_user_model()


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, bio="This is a test bio")

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.bio, "This is a test bio")
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEqual(str(self.profile), self.user.username)
