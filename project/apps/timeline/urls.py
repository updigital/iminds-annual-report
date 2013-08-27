# coding: utf-8
from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect


urlpatterns = patterns('project.apps.timeline.views',

	(r'^en/(?P<slug>[\w_-]+)/$', 'report_en'),
	(r'^nl/(?P<slug>[\w_-]+)/$', 'report_nl'),

	# January
	(r'^en/2012/milestone/january', 'milestone_january_en'),
	(r'^nl/2012/milestone/january', 'milestone_january_nl'),

	#February
	(r'^en/2012/milestone/february', 'milestone_february_en'),
	(r'^nl/2012/milestone/february', 'milestone_february_nl'),

	(r'^en/2012/highlight/february', 'highlight_february_en'),
	(r'^nl/2012/highlight/february', 'highlight_february_nl'),

	#March
	(r'^en/2012/milestone/march', 'milestone_march_en'),
	(r'^nl/2012/milestone/march', 'milestone_march_nl'),

	(r'^en/2012/highlight/march', 'highlight_march_en'),
	(r'^nl/2012/highlight/march', 'highlight_march_nl'),

	#April
	(r'^en/2012/milestone/april', 'milestone_april_en'),
	(r'^nl/2012/milestone/april', 'milestone_april_nl'),

	(r'^en/2012/highlight/april', 'highlight_april_en'),
	(r'^nl/2012/highlight/april', 'highlight_april_nl'),

	(r'^en/2012/highlight-02/april', 'highlight_april_02_en'),
	(r'^nl/2012/highlight-02/april', 'highlight_april_02_nl'),

	#May
	(r'^en/2012/milestone/may', 'milestone_may_en'),
	(r'^nl/2012/milestone/may', 'milestone_may_nl'),

	(r'^en/2012/highlight/may', 'highlight_may_en'),
	(r'^nl/2012/highlight/may', 'highlight_may_nl'),

	#June
	(r'^en/2012/highlight/june', 'highlight_june_en'),
	(r'^nl/2012/highlight/june', 'highlight_june_nl'),

	(r'^en/2012/highlight-02/june', 'highlight_june_02_en'),
	(r'^nl/2012/highlight-02/june', 'highlight_june_02_nl'),

	#July
	(r'^en/2012/highlight/july', 'highlight_july_en'),
	(r'^nl/2012/highlight/july', 'highlight_july_nl'),

	#August
	(r'^en/2012/highlight/august', 'highlight_august_en'),
	(r'^nl/2012/highlight/august', 'highlight_august_nl'),

	#September
	(r'^en/2012/milestone/september', 'milestone_september_en'),
	(r'^nl/2012/milestone/september', 'milestone_september_nl'),

	(r'^en/2012/highlight/september', 'highlight_september_en'),
	(r'^nl/2012/highlight/september', 'highlight_september_nl'),

	#October
	(r'^en/2012/milestone/october-02', 'milestone_october_02_en'),
	(r'^nl/2012/milestone/october-02', 'milestone_october_02_nl'),
	
	(r'^en/2012/milestone/october', 'milestone_october_en'),
	(r'^nl/2012/milestone/october', 'milestone_october_nl'),

	(r'^en/2012/highlight/october-02', 'highlight_october_02_en'),
	(r'^nl/2012/highlight/october-02', 'highlight_october_02_nl'),

	(r'^en/2012/highlight/october', 'highlight_october_en'),
	(r'^nl/2012/highlight/october', 'highlight_october_nl'),

	

	#November
	(r'^en/2012/milestone/november', 'milestone_november_en'),
	(r'^nl/2012/milestone/november', 'milestone_november_nl'),

	#December
	(r'^en/2012/milestone/december', 'milestone_december_en'),
	(r'^nl/2012/milestone/december', 'milestone_december_nl'),

	(r'^en/2012/highlight/december', 'highlight_december_en'),
	(r'^nl/2012/highlight/december', 'highlight_december_nl'),

	(r'^', lambda x: HttpResponseRedirect('/en/2012/')),
)