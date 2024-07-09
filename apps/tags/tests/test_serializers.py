from django.test import TestCase

from ..models import Tag
from ..serializers import TagSerializer


class TagSerializerTests(TestCase):
    def setUp(self):
        self.tag_data = {"name": "Test Tag"}

    def test_tag_serializer_create(self):
        serializer = TagSerializer(data=self.tag_data)
        self.assertTrue(serializer.is_valid())
        tag = serializer.save()
        self.assertEqual(tag.name, self.tag_data["name"])

    def test_tag_serializer_update(self):
        tag = Tag.objects.create(name="Old Tag Name")
        updated_data = {"name": "Updated Tag Name"}
        serializer = TagSerializer(tag, data=updated_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_tag = serializer.save()
        self.assertEqual(updated_tag.name, updated_data["name"])
