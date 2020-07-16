# Generated by Django 2.0.6 on 2020-07-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户id')),
                ('user_ip', models.CharField(max_length=20, verbose_name='用户ip')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('user_password', models.CharField(max_length=15, verbose_name='用户密码')),
                ('user_email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('user_profile_photo', models.ImageField(upload_to='user_head', verbose_name='用户头像')),
                ('user_registration_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_birthday', models.CharField(max_length=20, verbose_name='用户生日')),
                ('user_age', models.SmallIntegerField(verbose_name='用户年龄')),
                ('user_telephone_number', models.ImageField(max_length=11, upload_to='', verbose_name='用户手机号')),
                ('user_nickname', models.CharField(max_length=20, verbose_name='用户昵称')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'kxj_users',
            },
        ),
    ]
