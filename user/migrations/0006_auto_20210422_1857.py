# Generated by Django 3.2 on 2021-04-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210422_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fansNum',
            field=models.IntegerField(default=0, verbose_name='粉丝数量'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='noticeNum',
            field=models.IntegerField(default=0, verbose_name='关注数量'),
        ),
    ]