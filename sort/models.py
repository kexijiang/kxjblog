from django.db import models
from articles.models import Articles
# Create your models here.


class Sort(models.Model):
    sort_id = models.AutoField(primary_key=True, verbose_name='分类id')
    sort_name = models.CharField(max_length=50, verbose_name='分类名称', null=True)
    sort_description = models.CharField(max_length=50, verbose_name='分类描述', null=True)
    parent_sort_id = models.BigIntegerField(verbose_name='父分类id', null=True)

    class Meta:
        db_table = 'kxj_sort'
        verbose_name = '分类表'
        verbose_name_plural = verbose_name


class Article_sort(models.Model):
    article = models.ForeignKey('articles.Articles', on_delete=models.CASCADE, verbose_name='博文id')
    sort = models.ForeignKey('sort.Sort', on_delete=models.CASCADE, verbose_name='分类id')

    class Meta:
        db_table = 'kxj_article_sort'
        verbose_name = '博文设置分类表'
        verbose_name_plural = verbose_name


