# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.ll),
    url(r'^Projects/$',views.Projects,name='Projects'),
    url(r'^Del/$',views.Del,name='Del'),
    url(r'^Createproject/$',views.Createproject,name='Createproject'),
    url(r'^Zeng/$',views.Zeng,name='Zeng'),
    url(r'^Bj/$',views.project_bj,name='Bj'),
    url(r'^Project/$',views.Project,name='Project'),
    url(r'^Projectbj/$',views.Projectbj,name='Projectbj'),
    url(r'^User/$',views.User,name='User'),
    url(r'^Group/$',views.Group,name='Group'),
    url(r'^Role/$',views.Role,name='Role'),
    url(r'^Sl/$',views.Sl,name='Sl'),
    url(r'^Createsx/$',views.Createsx,name='Createsx'),
    url(r'^Qd/$',views.Qd,name='Qd'),
    url(r'^gb/$',views.gb,name='gb'),
    url(r'^sl_del/$',views.sl_del,name='sl_del'),
    url(r'^yx/$',views.yx,name='yx'),
    url(r'^image_add/$',views.image_add,name='image_add'),
    url(r'^jing/$',views.jing,name='jing'),
    url(r'^jing_del/$',views.jing_del,name='jing_del'),
    url(r'^cq/$',views.cq,name='cq'),
    url(r'^sl_bj/$',views.sl_bj,name='sl_bj'),
    url(r'^slbj/$',views.slbj,name='slbj'),
]
