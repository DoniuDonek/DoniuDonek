from django.test import TestCase
from category.models import Category

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            category_name='Example',
            slug='example',
            description='This is an example category.',
        )

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), self.category.category_name)
    
    def test_category_get_url(self):
        self.assertEqual(self.category.get_url(), '/store/category/example/')

    def test_category_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "categories")