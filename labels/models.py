from django.db import models
from articles.models import Articles

# Create your models here.
class Labels(models.Model):
    label_id = models.AutoField(primary_key=True, verbose_name='标签表id')
    label_name = models.CharField(max_length=20, verbose_name='标签名称')
    label_alias = models.CharField(max_length=20, verbose_name='标签别名')
    label_description = models.CharField(max_length=50, verbose_name='标签描述')

    class Meta:
        db_table = 'kxj_labels'
        verbose_name = '标签表'
        verbose_name_plural = verbose_name

class Article_label(models.Model):
    article = models.ForeignKey('articles.Articles', on_delete=models.CASCADE, verbose_name='博文id')
    label = models.ForeignKey('labels.Labels', on_delete=models.CASCADE, verbose_name='标签id')

    class Meta:
        db_table = 'kxj_article_label'
        verbose_name = '博文设置标签表'
        verbose_name_plural = verbose_name
