# coding:utf-8
from __future__ import unicode_literals

from django.db import models
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 博客文章正文

    # python2使用__unicode__, python3使用__str__
    def __str__(self):
        return self.title

    class Meta:  # '-'表示按时间降序
        ordering = ['-date_time']
