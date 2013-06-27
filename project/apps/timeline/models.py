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
	created_at = models.DateTimeField(auto_now=True)

	year = models.CharField(max_length=4)

	description_en = models.TextField(max_length=200, verbose_name=u'Description (en)')
	description_nl = models.TextField(max_length=200, verbose_name=u'Signalement (nl)')
	pdf_en = models.FileField(upload_to='pdf', verbose_name=u'PDF (en)')
	pdf_nl = models.FileField(upload_to='pdf', verbose_name=u'PDF (nl)')
	
	class Meta:
		verbose_name = _(u'Annual Report')
		verbose_name_plural = _(u'Annual Report')

	def __unicode__(self):
		return self.year

class Month(models.Model):
	created_at = models.DateTimeField(auto_now=True)

	MONTH_EN = (
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

	MONTH_NL = (
		('01', _('Januari')),
		('02', _('Februari')),
		('03', _('Maart')),
		('04', _('April')),
		('05', _('Mei')),
		('06', _('Juni')),
		('07', _('Juli')),
		('08', _('Augustus')),
		('09', _('September')),
		('10', _('Oktober')),
		('11', _('November')),
		('12', _('December')),
	)
	report = models.ForeignKey('Report')
	month_en = models.CharField(max_length=2, choices=MONTH_EN, verbose_name=u'Month (en)')
	month_nl = models.CharField(max_length=2, choices=MONTH_NL, verbose_name=u'Maand (nl)')
	title_en = models.CharField(_('Title (en)'), max_length=140)
	title_nl = models.CharField(_('Titel (nl)'), max_length=140)
	description_en = models.TextField(_('Description (en)'), max_length=140)
	description_nl = models.TextField(_('Signalement (nl)'), max_length=140)
	milestone = ImageWithThumbsField(_('Milestone'),
			upload_to='images',
			sizes=((160,160),(200,200)))
	pdf_en = models.FileField(upload_to='PDF (en)')
	pdf_nl = models.FileField(upload_to='PDF (nl)')

	content_en = models.TextField(_('Content (en)'), max_length=840)
	content_nl = models.TextField(_('Inhoud (nl)'), max_length=840)

	def __unicode__(self):
		return self.title_en

def slug_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.year)

signals.pre_save.connect(slug_pre_save, sender=Report)

