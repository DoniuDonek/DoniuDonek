from django.test import TestCase
from accounts.forms import RegistrationForm, UserForm, UserProfile, UserProfileForm
from accounts.models import Account
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.core.files import File
import os
# import pdb

class TestRegistrationForm(TestCase):
    def test_form_valid(self):
        form = RegistrationForm({
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'email': 'john.doe@example.com',
            'password': 'password',
            'confirm_password': 'password',
        })
        self.assertTrue(form.is_valid())
        
    def test_form_invalid(self):
        form = RegistrationForm({
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'email': 'john.doe@example.com',
            'password': 'password',
            'confirm_password': 'password123',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['__all__'], ['Password must be the same'])

class TestUserForm(TestCase):
    def test_form_valid(self):
        form = UserForm({
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
        })
        self.assertTrue(form.is_valid())
        
    def test_form_invalid(self):
        form = UserForm({
            'first_name': '',
            'last_name': 'Doe',
            'phone_number': '1234567890',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], ['This field is required.'])
    
    def test_form_save(self):
        form = UserForm({
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
        })

        self.assertTrue(form.is_valid())
        form.save()
        account = Account.objects.get(first_name='John')
        self.assertEqual(account.last_name, 'Doe')
        self.assertEqual(account.phone_number, '1234567890')
        # Created an instance of the form and passed valid data to it and then called save method on it. 
        # After that,  query db for the Account object created and assert that it has the same data that was passed to the form.

class TestUserProfileForm(TestCase):
    def setUp(self):
        path = os.path.join(settings.BASE_DIR, 'accounts', 'tests', 'test.jpg')
        self.image = SimpleUploadedFile(
            name='test.jpg',
            content=open(path, 'rb').read(),
            content_type='image/jpeg'
        )

    def test_valid_form(self):
        form_data = {
            'address_line_1': 'Test Address 1',
            'address_line_2': 'Test Address 2',
            'country': 'Test Country',
            'state': 'Test State',
            'city': 'Test City',
            'profile_picture': self.image,
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_valid_image(self):
        image = SimpleUploadedFile("valid_image.jpg", b"file_content", content_type="image/jpeg")
        form_data = {
            'address_line_1': 'test address',
            'country': 'test country',
            'state': 'test state',
            'city': 'test city',
            'profile_picture': image,
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    # def test_form_with_invalid_image(self):
    #     image = SimpleUploadedFile("valid_image.txt", b"file_content", content_type="text/plain")
    #     form_data = {
    #         'address_line_1': 'test address',
    #         'country': 'test country',
    #         'state': 'test state',
    #         'city': 'test city',
    #         'profile_picture': image,
    #     }
    #     form = UserProfileForm(data=form_data)
    #     self.assertFalse(form.is_valid())
    #     print(form.errors)
    #     self.assertEqual(form.errors['profile_picture'], ["Invalid image file. Only .jpg and .bmp files are allowed"])






    




       
    # def test_form_save(self):   # test is good, but not working... need upgrade
    #     form = UserProfileForm({
    #         'address_line_1': 'Test street 123',
    #         'address_line_2': '',
    #         'country': 'Test country',
    #         'state': 'Test state',
    #         'city': 'Test city',
    #     })
    #     form.user = self.user 
    #     self.assertTrue(form.is_valid())
    #     form.save()
    #     profile = UserProfile.objects.get(address_line_1='Test street 123')
    #     self.assertEqual(profile.address_line_2, '')
    #     self.assertEqual(profile.country, 'Test country')
    #     self.assertEqual(profile.state, 'Test state')
    #     self.assertEqual(profile.city, 'Test city')
        