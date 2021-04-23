# Generated by Django 3.2 on 2021-04-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=16, verbose_name='电话')),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('birth_time', models.TimeField(verbose_name='出生时间')),
                ('birth_place', models.CharField(max_length=50, verbose_name='出生地')),
                ('create_time', models.TimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_time', models.TimeField(verbose_name='最后更新时间')),
                ('sex', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=8, verbose_name='性别')),
                ('avatar', models.CharField(max_length=256, verbose_name='头像')),
                ('email', models.CharField(max_length=64, verbose_name='邮箱')),
                ('id_card', models.CharField(max_length=32, verbose_name='身份ID')),
            ],
        ),
    ]