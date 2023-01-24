"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model  # refernce to custome model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['Test2@example.com', 'Test2@example.com'],
            ['Test3@example.COM', 'Test3@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'pass123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='', password='pass')

    def test_create_superuser(self):
        email = 'test@example.com'
        password = 'testpass1234'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
