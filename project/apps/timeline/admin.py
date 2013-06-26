# coding: utf-8
from django.contrib import admin
from django import forms
from models import *
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.utils.datetime_safe import datetime

class MonthAdmin(admin.ModelAdmin):
	list_display = ('report', 'month', 'title', 'description', 'milestone', 'created_at')
	data_hierarchy = 'name'
	search_fields = ('name',)
	list_filter = ['report', 'month', 'title', 'description', 'milestone', 'created_at']

	def subscribe_today(self, obj):
		return obj.publication.date() == datetime.today().date()

	subscribe_today.short_description = _(u'Inscrito Hoje?')
	subscribe_today.boolean = True

class MonthInline(admin.TabularInline):
	model = Month
	extra = 1

class ReportAdmin(admin.ModelAdmin):
	list_display = ('year', 'description', 'created_at')
	data_hierarchy = 'year'
	search_fields = ('year',)
	list_filter = ['created_at', 'year']

	inlines = [MonthInline,]

admin.site.register(Report, ReportAdmin)
admin.site.register(Month, MonthAdmin)