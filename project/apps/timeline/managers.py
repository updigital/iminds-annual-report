# coding: utf-8
from django.db import models


class FacebookSocialManager(models.Manager):
	def get_query_set(self):
		qs = super(FacebookSocialManager, self).get_query_set()
		qs = qs.filter(kind='FB')
		return qs