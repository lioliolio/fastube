from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^new/$', PostCreateFormView.as_view(), name="create"),
]