from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    likedTweets = models.ManyToManyField('Tweet', related_name='hasLiked', blank=True)
    following = models.ManyToManyField('Account', related_name='followers', blank=True)

    def __str__(self):
        return self.user.username


class Tweet(models.Model):
    content = models.CharField(max_length=180)
    poster = models.ForeignKey('Account', related_name='tweets', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.timestamp, self.content, self.poster)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
