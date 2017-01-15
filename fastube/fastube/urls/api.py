from django.conf.urls import include, url

from posts.api import *


urlpatterns = [
    url(r'^posts/$', include([
        url(r'^$', PostListAPIView.as_view(), name="list"),
    ], namespace="posts")),
]
