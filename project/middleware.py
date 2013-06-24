# coding: utf-8
from django.contrib.auth.views import redirect_to_login
from django.conf import settings

class DeveloperMiddleware(object):

    def process_request(self, request):
        if settings.IS_DEV and not request.user.is_staff and '/login/' != request.path:
        	return redirect_to_login(request.path)