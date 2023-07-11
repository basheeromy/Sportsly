"""Tests for models."""

from django.test import TestCase
from django.contrib.auth import get_user_model
from faker import Faker



class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""

        email = 'test@example.com'
        password = 'testpass123'
        fake = Faker()
        random_mobile_number = fake.numerify(text='############')
        user = get_user_model().objects.create_user(
            email=email,
            mobile=random_mobile_number,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))



    def test_new_user_email_normalized(self):
        """Test email normalized for new user."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]


        for email, expected in sample_emails:
            fake = Faker()
            random_mobile_number = fake.numerify(text='############')
            user = get_user_model().objects.create_user(
                email, random_mobile_number, 'sample123'
                )
            self.assertEqual(user.email, expected)
