from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from datetime import datetime
from django.db.models.expressions import Case
from django.db.models.fields import related
from django.utils import timezone


class User(AbstractUser):
    pass


class Profile(models.Model):
    """
    The specific content of the user includes Bio, Photo, Background Photo
    PK: user_id, username, followers, following
    """

    name = models.CharField(max_length=20)
    bio = models.CharField(max_length=256, blank=True)
    # TODO change the settings to save the photos to network/static/media/img
    photo = models.ImageField(
        default="./media/network/img/default_user_photo.jpg")
    background_photo = models.ImageField(
        default="./media/network/img/black_background.jpg")
    user = models.ForeignKey(User, on_delete=CASCADE)
    profile_id = models.AutoField(primary_key=True)

    followers = models.ManyToManyField(
        User, default=None, blank=True, related_name="target")
    following = models.ManyToManyField(
        User, default=None, blank=True, related_name="not_target")

    def get_following_count(self):
        return len(self.following.all())

    def get_follower_count(self):
        return len(self.followers.all())

    def get_like_count(self):
        return len(self.liked.all())

    def __str__(self):
        return f"Profile name: {self.name}"


class Posts(models.Model):
    """User created Posts Model linked through the profile"""

    post_id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=256)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    liked = models.ManyToManyField(
        User, default=None, blank=True, related_name="post_likes")
    timestamp = models.DateTimeField(auto_now_add=True)
    # post must reference the profile that is creating it
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f"User: {self.user.username}, ID: {self.post_id}, Content: {self.content[:50]}"


class LikedPosts(models.Model):
    # posts the user has liked
    # the user
    user = models.ForeignKey(User, on_delete=CASCADE)
    post = models.ForeignKey(Posts, on_delete=CASCADE)

    def __str__(self):
        return f"User: {self.user.username}, Post ID: {self.post.post_id}"
