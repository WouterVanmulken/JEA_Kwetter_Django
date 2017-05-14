from django.contrib.auth.models import User, Group
from rest_framework import serializers
from kwetter.models import Tweet, Account


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ('url', 'content', 'timestamp', 'poster', 'hasLiked')


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    tweets = TweetSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('url', 'user', 'first_name', 'last_name', 'bio',
                  'tweets', 'likedTweets', 'following', 'followers')
