from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
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
