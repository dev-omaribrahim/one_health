from django.test import TestCase
from ..models import Category
from ..serializers import CategorySerializer


class CategorySerializerTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.serializer = CategorySerializer(instance=self.category)

    def test_category_serializer_data(self):
        data = self.serializer.data
        self.assertEqual(data['name'], 'Test Category')
        self.assertEqual(data['slug'], self.category.slug)
