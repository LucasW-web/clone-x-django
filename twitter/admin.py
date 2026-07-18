from django.contrib import admin
from .models import Profile, Tweet, Follow, Like, Comment

admin.site.register(Profile)
admin.site.register(Tweet)
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Comment)