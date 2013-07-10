# coding: utf-8
from django.contrib import admin
from django import forms
from models import *
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.utils.datetime_safe import datetime


class MonthAdmin(admin.ModelAdmin):
	list_display = ('report', 'language', 'month', 'title', 'description', 'created_at')
	data_hierarchy = 'name'
	search_fields = ('title', 'description')
	list_filter = ['report', 'language', 'month', 'created_at']

	def subscribe_today(self, obj):
		return obj.publication.date() == datetime.today().date()

	subscribe_today.short_description = _(u'Inscrito Hoje?')
	subscribe_today.boolean = True

class ReportInline(admin.StackedInline):
    model = Month
    extra = 1
    max_num = 24

class ReportAdmin(admin.ModelAdmin):
	list_display = ('year', 'language', 'created_at')
	data_hierarchy = 'year'
	search_fields = ('year',)
	list_filter = ['year', 'language', 'created_at']
	inlines = [ReportInline, ]

admin.site.register(Report, ReportAdmin)
admin.site.register(Month, MonthAdmin)