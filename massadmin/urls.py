#coding=utf-8
#--- Author: Dmitri Patrakov <traditio@gmail.com>
from django.conf.urls.defaults import *
# import new


urlpatterns = patterns('',
    (r'(?P<app_name>[a-z]+)/(?P<model_name>[a-z]+)-masschange/(?P<object_ids>[0-9,]+)/$',
     'server.massadmin.massadmin.mass_change_view'),
                # (r'(?P<whatever>.*)', 'massadmin.massadmin.redirect_to_admin')
)