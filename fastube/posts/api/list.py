from django.views.generic import View
from django.http import HttpResponse


class PostListAPIView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("posts:list")
