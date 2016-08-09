#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-09 19:39:57
# @Author  : moling (365024424@qq.com)
# @Link    : http://www.qiangtaoli.com
# @Version : $Id$

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello$', views.hello),
]
