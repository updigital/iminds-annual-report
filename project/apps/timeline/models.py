# coding: utf-8
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from thumbs import ImageWithThumbsField
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _
from django.db.models import signals
from django.template.defaultfilters import slugify

LANGUAGE = (
		('EN', _('English')),
		('NL', _('Dutch')),
	)

class Report(models.Model):
	language = models.CharField(max_length=2, choices=LANGUAGE)
	created_at = models.DateTimeField(auto_now=True)

	slug = models.SlugField(max_length=4, unique=True, editable=False)
	year = models.CharField(max_length=4, help_text='This is year', unique=True)

	description = models.TextField(max_length=200)
	pdf = models.FileField(upload_to='pdf')

	pdf_image = ImageWithThumbsField(
			upload_to='images',
			sizes=((105,120),))
	
	class Meta:
		verbose_name = _(u'Annual Report')
		verbose_name_plural = _(u'Annual Report')

	def __unicode__(self):
		return self.year

class Month(models.Model):
	language = models.CharField(max_length=2, choices=LANGUAGE)
	created_at = models.DateTimeField(auto_now=True)

	MONTH = (
		('01', _('January')),
		('02', _('February')),
		('03', _('March')),
		('04', _('April')),
		('05', _('May')),
		('06', _('June')),
		('07', _('July')),
		('08', _('August')),
		('09', _('September')),
		('10', _('October')),
		('11', _('November')),
		('12', _('December')),
	)

	report = models.ForeignKey('Report')
	month = models.CharField(max_length=2, choices=MONTH)
	title = models.CharField(max_length=140)
	description = models.TextField(max_length=140)
	milestone = ImageWithThumbsField(
			upload_to='images',
			sizes=((160,160),(200,200)))

	content = RedactorField(verbose_name=u'Content', help_text='&nbsp;*Use HTML mode')

	def __unicode__(self):
		return self.title

def slug_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.year)

signals.pre_save.connect(slug_pre_save, sender=Report)
