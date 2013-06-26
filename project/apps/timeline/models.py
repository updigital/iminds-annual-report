# coding: utf-8
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from thumbs import ImageWithThumbsField
from django.utils.translation import ugettext_lazy as _
from django.db.models import signals
from django.template.defaultfilters import slugify
from managers import FacebookSocialManager

class Report(models.Model):
	slug = models.SlugField(max_length=100, editable=False, unique=True)
	created_at = models.DateTimeField()

	year = models.CharField(max_length=4)
	description = models.TextField(max_length=200)
	pdf = models.FileField(upload_to='pdf')
	
	class Meta:
		verbose_name = _(u'Annual Report')
		verbose_name_plural = _(u'Annual Report')

	def __unicode__(self):
		return self.year

class Month(models.Model):
	created_at = models.DateTimeField()
	MONTH = (
		('1', _('January')),
		('2', _('February')),
		('3', _('March')),
		('4', _('April')),
		('5', _('May')),
		('6', _('June')),
		('7', _('July')),
		('8', _('August')),
		('9', _('September')),
		('10', _('October')),
		('11', _('November')),
		('12', _('December')),
	)
	report = models.ForeignKey('Report')
	month = models.CharField(_('Month'), max_length=2, choices=MONTH)
	title = models.CharField(_('Title'), max_length=140)
	description = models.TextField(_('Description'), max_length=140)
	milestone = ImageWithThumbsField(_('Milestone'),
			upload_to='images',
			sizes=((160,160),(200,200)))
	pdf = models.FileField(upload_to='pdf')

	objects = models.Manager()
	facebooks = FacebookSocialManager()

	def __unicode__(self):
		return self.title

def slug_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.year)

signals.pre_save.connect(slug_pre_save, sender=Report)

