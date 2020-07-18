from django.db import models
from tinymce.models import HTMLField


from articles.models import Articles
# Create your models here.
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, verbose_name='评论id')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户id', null=False)
    article = models.ForeignKey('articles.Articles', on_delete=models.CASCADE, verbose_name='博文id', null=False)
    comment_like_count = models.BigIntegerField(verbose_name='评论点赞数', null=True)
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name='评论创建时间')
    comment_content = HTMLField(blank=True, verbose_name='评论内容', null=True)
    parent_comment_id = models.BigIntegerField(verbose_name='父评论id', null=True)

    class Meta:
        db_table = 'kxj_comments'
        verbose_name = '评论表'
        verbose_name_plural = verbose_name