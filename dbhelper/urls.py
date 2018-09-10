# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'dbhelper.views',
    url(r'^dump/$', 'dump_db'),
    url(r'^drop_table/$', 'drop_table'),
    url(r'^init_data/$', 'init_data'),
)
