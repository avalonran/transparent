# Generated by Django 3.2 on 2021-04-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210422_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_time',
            field=models.TimeField(auto_now=True, verbose_name='最后更新时间'),
        ),
    ]
