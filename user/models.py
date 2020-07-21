from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser, models.Model):
    # user_id = models.AutoField(primary_key=True, verbose_name='用户id')
    #     # user_ip = models.CharField(max_length=20, verbose_name='用户ip', null=True)
    #     # user_name = models.CharField(max_length=20, verbose_name='用户名')
    #     # user_password = models.CharField(max_length=15, verbose_name='用户密码')
    #     # user_email = models.EmailField(verbose_name='用户邮箱', null=True)
    #     # user_profile_photo = models.ImageField(upload_to='user_head', verbose_name='用户头像', null=True)
    #     # user_registration_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True)
    #     # user_birthday = models.CharField(max_length=20, verbose_name='用户生日', null=True)
    #     # user_age = models.SmallIntegerField(verbose_name='用户年龄', null=True)
    #     # user_telephone_number = models.ImageField(max_length=11, verbose_name='用户手机号', null=True)
    #     # user_nickname = models.CharField(max_length=20, verbose_name='用户昵称', null=True)

    class Meta:
        db_table = 'kxj_users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name