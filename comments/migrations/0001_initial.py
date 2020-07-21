# Generated by Django 2.2 on 2020-07-19 08:32

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='评论id')),
                ('comment_like_count', models.BigIntegerField(null=True, verbose_name='评论点赞数')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='评论创建时间')),
                ('comment_content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='评论内容')),
                ('parent_comment_id', models.BigIntegerField(null=True, verbose_name='父评论id')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Articles', verbose_name='博文id')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
                'db_table': 'kxj_comments',
            },
        ),
    ]
