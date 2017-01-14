from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^new/$', PostCreateView.as_view(), name="create"),
    url(r'^confirm/$', PostCreateConfirmView.as_view(), name="confirm"),
]
