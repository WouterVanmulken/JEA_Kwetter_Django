# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-14 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwetter', '0003_account_likedtweets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='likedTweets',
        ),
        migrations.AddField(
            model_name='account',
            name='likedTweets',
            field=models.ManyToManyField(related_name='hasLiked', to='kwetter.Tweet'),
        ),
    ]