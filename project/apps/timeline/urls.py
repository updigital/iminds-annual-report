# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('project.apps.timeline.views',

	(r'^en/(?P<slug>[\w_-]+)/$', 'timeline_en'),
	(r'^nl/(?P<slug>[\w_-]+)/$', 'timeline_nl'),

	(r'^en/', 'list_timeline_en'),
	(r'^nl/', 'list_timeline_en'),
)