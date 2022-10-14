"""
Test models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class TestModels(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test create user with an email successful."""
        email = 'test@email.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Testing Emails are being normalized."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample12')
            self.assertEqual(user.email, expected)

    def test_create_superuser(self):
        """Testing create superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
