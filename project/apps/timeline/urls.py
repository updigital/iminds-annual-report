# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('project.apps.timeline.views',

	(r'^(?P<slug>[\w_-]+)/$', 'timeline'),
	(r'^', 'list_timeline'),
)