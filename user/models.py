import time
import datetime

from django.db import models





class User(models.Model):
    SEX = (('M', '男'), ('F', '女'))

    phone = models.CharField(max_length=16, verbose_name='电话')
    nickname = models.CharField(max_length=32, verbose_name='昵称')
    birth_time = models.DateTimeField(verbose_name='出生时间')
    birth_place = models.CharField(max_length=50, verbose_name='出生地')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别')
    avatar = models.CharField(max_length=256, verbose_name='头像')
    email = models.CharField(max_length=64, verbose_name='邮箱')
    id_card = models.CharField(max_length=32, verbose_name='身份ID')

    # _profile = None

    @property
    def age(self):
        #datetime.date() ，解决数据库时区不一致，不能相减的问题
        return (datetime.datetime.now().date() - self.birth_time.date()).days // 365

    @property
    def profile(self):
        # if self._profile is None:
        if not hasattr(self, '_profile '):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile


class Profile(models.Model):
    noticeNum = models.IntegerField(default=0, verbose_name='关注数量')
    fansNum = models.IntegerField(default=0, verbose_name='粉丝数量')
    location_city = models.CharField(max_length=16, verbose_name='所在城市')
