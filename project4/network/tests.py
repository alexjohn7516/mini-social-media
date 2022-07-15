from django.test import TestCase, Client
from .models import User, Profile, Posts
from .views import follow
from datetime import datetime


class ModelsTest(TestCase):
    """Test my django Model creation and linkage"""

    def test_user_creation(self):
        """Test the creation of a user"""

        user1 = User.objects.create(
            username="Jhuiice", password="Richman", email="foo@example.com")
        self.assertTrue(user1.username, "Jhuiice")

    def test_create_profile(self):
        """Tests the creation of a profile"""

        user1 = User.objects.create(
            username="Jhuiice", password="Richman", email="foo@example.com")
        profile1 = Profile.objects.create(
            name="", bio="", photo="", background_photo="", user=user1)
        self.assertEqual(profile1.user.username, "Jhuiice")
        self.assertEqual(profile1.name, "")

    def test_create_post(self):
        """Test the creation of Posts"""

        user1 = User.objects.create(
            username="Jhuiice", password="Richman", email="foo@example.com")
        posts1 = Posts.objects.create(
            content="This is a test from Django Tests", user=user1)
        self.assertEqual(posts1.content, "This is a test from Django Tests")
        self.assertEqual(posts1.user.username, "Jhuiice")

    def test_create_profile(self):
        user = User.objects.create_user(
            username="Jhuiice", password="Richman_24", email="foo@example.com")
        user.save()
        profile = Profile.objects.create(name=user.username, user=user)
        profile.save()
        self.assertEqual(profile.user.username, user.username)
        self.assertEqual(profile.name, user.username)

    def test_profile_following(self):
        """USER1 is attemptimg to follow USER2"""
        user1 = User.objects.create_user(
            username="Jhuiice", password="Richman_24", email="foo@example.com")
        user2 = User.objects.create_user(
            username="juice", password="Richman_24", email="bar@example.com")
        profile1 = Profile.objects.create(user=user1, name=user1.username)
        profile2 = Profile.objects.create(user=user2, name=user2.username)
        # profile2 is attempting to follow profile1
        if user2 not in profile1.following.all():
            # adds to followers list
            profile1.following.add(user2)
            profile2.followers.add(user1)
            self.assertEqual(user1 in profile2.followers.all(), True)
            self.assertEqual(user2 in profile1.following.all(), True)
        else:
            # removes followers list
            profile1.following.remove(user2)
            profile2.followers.remove(user1)
        profile1.save()
        profile2.save()
        self.assertIn(user2, profile1.following.all())
        self.assertIn(user1, profile2.followers.all())
        self.assertEqual(profile1.get_following_count(), 1)
        self.assertEqual(profile2.get_followers_count(), 1)
