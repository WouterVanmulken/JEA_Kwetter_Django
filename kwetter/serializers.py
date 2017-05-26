from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from kwetter.models import Tweet, Account


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    # tweets = TweetSerializer(many=True, read_only=True)

    # tweets = SlugRelatedField(many=True, read_only=True, slug_field='id')

    class Meta:
        model = Account
        fields = ('id', 'url', 'user', 'first_name', 'last_name', 'bio',
                  'tweets', 'likedTweets', 'following', 'followers')


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    hasLiked = AccountSerializer(many=True, read_only=True)

    # poster = AccountSerializer(many=False,read_only=True)
    # poster = SlugRelatedField(many=False,slug_field='id')
    class Meta:
        model = Tweet
        fields = ('id', 'url', 'content', 'timestamp', 'poster', 'hasLiked')


class Tweet2Serializer(serializers.HyperlinkedModelSerializer):
    hasLiked = AccountSerializer(many=True, read_only=True)
    poster = AccountSerializer(many=False, read_only=True)

    class Meta:
        model = Tweet
        fields = ('id', 'url', 'content', 'timestamp', 'poster', 'hasLiked')
