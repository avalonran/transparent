# Generated by Django 3.2 on 2021-04-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fansNum',
            field=models.IntegerField(verbose_name='粉丝数量'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='noticeNum',
            field=models.IntegerField(verbose_name='关注数量'),
        ),
    ]
