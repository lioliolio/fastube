from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', PostListView.as_view(), name="list"),

    url(r'^new/$', PostCreateView.as_view(), name="create"),
    url(r'^confirm/$', PostCreateConfirmView.as_view(), name="confirm"),

    url(r'^(?P<slug>\w+)/$', PostDetailView.as_view(), name="detail"),
]
