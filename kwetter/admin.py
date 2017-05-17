from django.contrib import admin

from kwetter.models import Account, Tweet


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'bio')
    list_filter = ('first_name', 'last_name')


admin.site.register(Account, AccountAdmin)


class TweetAdmin(admin.ModelAdmin):
    list_display = ('content', 'poster', 'timestamp')
    list_filter = ('content', 'poster', 'timestamp')


admin.site.register(Tweet, TweetAdmin)
