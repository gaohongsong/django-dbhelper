from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns(
    'db_helper.views',
    url(r'^dump_db/$', 'dump_db'),
    url(r'^drop_table/$', 'drop_table'),
    url(r'^init_data/$', 'init_data'),
)
