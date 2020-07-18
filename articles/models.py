from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Articles(models.Model):
    article_id = models.AutoField(primary_key=True, verbose_name='博文id')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户id')
    article_title = models.CharField(max_length=200, verbose_name='博文标题')
    article_introduce = models.CharField(max_length=200, verbose_name='博文简介', null=True)
    article_content = HTMLField(blank=True, verbose_name='博文内容')
    article_views = models.BigIntegerField(verbose_name='浏览量', default=0, null=True)
    article_comment_count = models.BigIntegerField(verbose_name='评论总数', default=0, null=True)
    article_date = models.DateTimeField(auto_now_add=True, verbose_name='发表时间', null=True)
    article_like_count = models.BigIntegerField(verbose_name='点赞数', default=0, null=True)

    class Meta:
        db_table = 'kxj_articles'
        verbose_name = '博文表'
        verbose_name_plural = verbose_name
