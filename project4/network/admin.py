from django.contrib import admin

from network.models import Posts, User, Profile, LikedPosts
# Register your models here.

admin.site.register(Posts)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(LikedPosts)
