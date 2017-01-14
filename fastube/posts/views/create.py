from django.shortcuts import render
from django.views.generic import View


class PostCreateFormView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "posts/new.html",
            context={},
        )
