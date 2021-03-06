"""jea_kwetter_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from kwetter import views

from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.authtoken import views as authorization_token_views
# schema_view = get_swagger_view(title='Kwetter')

API_TITLE = 'Kwetter'
API_DESCRIPTION = 'Kwetter api implementation in django'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tweets', views.TweetViewSet)
router.register(r'personaltweets/(?P<id>.+)', views.PersonalTweets,'personaltweets/')
# router.register(r'testaccount', views.TestAccountViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # url(r'^swagger/', schema_view),
    # url(r'^api-token-auth/', authorization_token_views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
