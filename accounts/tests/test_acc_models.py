from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Account, UserProfile, MyAccountManager

class AccountModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            first_name='Test',
            last_name='User',
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_created(self):
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_permissions(self):
        self.assertFalse(self.user.is_admin)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)        
        
        self.assertFalse(self.user.is_active)
        self.assertFalse(self.user.has_perm('view_user'))

    def test_user_str(self):
        self.assertEqual(str(self.user), 'test@example.com')
        
    def test_user_full_name(self):
        self.assertEqual(self.user.full_name(), 'Test User')

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            first_name='Test',
            last_name='User',
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            address_line_1='123 Main St.',
            country='United States',
            state='California',
            city='Los Angeles',
        )

    def test_user_profile_created(self):
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.address_line_1, '123 Main St.')
        self.assertEqual(self.user_profile.country, 'United States')
        self.assertEqual(self.user_profile.state, 'California')
        self.assertEqual(self.user_profile.city, 'Los Angeles')

    def test_user_profile_str(self):
        self.assertEqual(str(self.user_profile), self.user.first_name)
    
    def test_user_profile_full_address(self):
        self.assertEqual(self.user_profile.full_address(), '123 Main St. ')

class CreateSuperuserTest(TestCase):

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='super@user.com', 
            password='foo',
            first_name='John',
            last_name='Doe',
            username='Donek',
        )
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

     

# class MyAccountManagerTest(TestCase): # need some repairs
#     manager = MyAccountManager()

#     def setUp(self):
#         pass

#     def test_create_user(self):
#         # Test creating a user with all required fields
#         self.user = self.manager.create_user(
#             first_name='John',
#             last_name='Doe',
#             email='johndoe@example.com',
#             username='johndoe',
#             password='password123'
#         )
#         self.assertIsNotNone(self.user)
#         self.assertIsInstance(self.user, get_user_model())
#         self.assertEqual(self.user.first_name, 'John')
#         self.assertEqual(self.user.last_name, 'Doe')
#         self.assertEqual(self.user.email, 'johndoe@example.com')
#         self.assertEqual(self.user.username, 'johndoe')
#         self.assertTrue(self.user.check_password('password123'))