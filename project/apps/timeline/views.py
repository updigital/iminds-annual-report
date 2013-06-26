# coding: utf-8
from django.views.generic.simple import direct_to_template
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import *


def list_timeline(request):
    return direct_to_template(request, 'list_timeline.html',
        {'report':Report.objects.all(),},
    )

# def timeline_year(request, slug):
#     report = Report.objects.get(slug=slug)
#     return direct_to_template(request, 'home.html',
#         {'report':Report.objects.all()[0:],
#         'january':Month.objects.filter(month=1)[0:],
#         'music':Report.objects.filter(month=0)[0:],
#         'literature':Report.objects.filter(month=0)[0:],
#         'art':Report.objects.filter(month=0)[0:],
#         'cinema':Report.objects.filter(month=0)[0:],
#         'moda':Report.objects.filter(month=0)[0:],
#         'events':Report.objects.filter(month=0)[0:]},
#     )

def timeline(request, slug):
    report = Report.objects.filter(slug=slug)
    january = Month.objects.filter(report=report)
    payload = { 'report':report, 'january':january}
    return render(request, 'home.html', payload)

# def home(request, slug):
#     report = Report.objects.filter(slug=slug)
#     return render_to_response('home.html', locals(),
#         context_instance=RequestContext(request))