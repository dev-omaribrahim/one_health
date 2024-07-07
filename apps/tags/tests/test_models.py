from django.test import TestCase
from ..models import Tag


class TagModelTests(TestCase):
    def test_create_tag(self):
        tag = Tag.objects.create(name='Test Tag 1')
        self.assertEqual(tag.name, 'Test Tag 1')
        self.assertIsNotNone(tag.slug)  # Ensure slug field is populated

    def test_unique_slug_generation(self):
        tag1 = Tag.objects.create(name='Test Tag 1')
        tag2 = Tag.objects.create(name='Test Tag 2')

        self.assertNotEqual(tag1.slug, tag2.slug)  # Ensure slugs are unique

    # Add more tests as needed for Tag model methods or edge cases

