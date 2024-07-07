from django.test import TestCase
from django.utils.text import slugify
from ..models import Category


class CategoryModelTestCase(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_creation(self):
        category = Category.objects.get(name='Test Category')
        self.assertEqual(category.name, 'Test Category')
        self.assertEqual(category.slug, slugify(category.name))

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Test Category')
