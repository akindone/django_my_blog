# coding=utf-8
"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from article.views import home, detail
from article import views as article_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),  # 使用设置好的url进入admin页面
    url(r'^$', home, name='home'),
    url(r'^(?P<my_args>\d+)/$', article_views.detail, name='detail'),
    # the ?P<args_name>  args_name must be the same with the views.py function
    url(r'^test/$', article_views.test, name='test'),  # 不要忘了 name＝
]
