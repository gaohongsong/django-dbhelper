# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'db_helper.views',
    url(r'^dump_db/$', 'dump_db'),
    url(r'^drop_table/$', 'drop_table'),
    url(r'^init_data/$', 'init_data'),
)
