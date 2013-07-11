# coding: utf-8
from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect


urlpatterns = patterns('project.apps.timeline.views',

	(r'^en/(?P<slug>[\w_-]+)/$', 'report_en'),
	(r'^nl/(?P<slug>[\w_-]+)/$', 'report_nl'),

	(r'^en/', 'list_en'),
	(r'^nl/', 'list_nl'),

	(r'^', lambda x: HttpResponseRedirect('/en/2012/')),
)