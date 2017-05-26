from django.shortcuts import render
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from kwetter.models import Tweet, Account
# from serializers import UserSerializer, GroupSerializer, TweetSerializer, AccountSerializer
from kwetter.serializers import UserSerializer, GroupSerializer, TweetSerializer, AccountSerializer, Tweet2Serializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ('name',)


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    filter_fields = ('poster',)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('content',)
    search_fields = ('content',)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('first_name', 'last_name', 'bio')
    search_fields = ('first_name', 'last_name', 'bio')


class PersonalTweets(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        id = self.kwargs['id']
        current_user = Account.objects.filter(id=id).first()
        following = current_user.following.all()
        return Tweet.objects.filter(Q(poster_id=id) | Q(poster__in=following)).order_by('timestamp').reverse()
    serializer_class = Tweet2Serializer
