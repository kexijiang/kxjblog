from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from articles.models import Articles
from comments.models import Comment
from user.models import User


class CommentView(View):
    """显示评论页面"""
    def get(self, request):
        user = request.get('user')
        if user is not None:
            return redirect(reverse('user:index',))

    """提交评论内容"""
    def post(self, request):
        # 1.接收数据
        # article 博文id user 用户id comment_content 评论内容
        article = request.POST.get('article')
        user = request.POST.get('user')
        comment_content = request.POST.get('comment_content')
        # 2.校验数据
        print([article, user, comment_content])
        if not all([article, user, comment_content]):
            return {'res': 1, 'errmsg': '参数不足!'}
        # 3.业务处理
        article_id = article
        article = Articles.objects.get(article_id=article_id)
        user = User.objects.get(id=user)
        comment = Comment()
        comment.article = article
        comment.user = user
        comment.comment_content = comment_content
        comment.save()
        print("处理完成！")
        # 4.返回应答
        comments = Comment.objects.filter(article=article_id).order_by('-comment_date')
        return HttpResponse(comments)
