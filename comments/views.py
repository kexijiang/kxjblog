from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View


class CommentView(View):
    """显示评论页面"""
    def get(self, request):
        user = request.get('user')
        if user is not None:
            return redirect(reverse('user:index',))
