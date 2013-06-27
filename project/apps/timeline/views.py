# coding: utf-8
from django.views.generic.simple import direct_to_template
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import *


def list_timeline_en(request):
    return direct_to_template(request, 'list_timeline.html',
        {'report':Report.objects.all(),},
    )

def list_timeline_nl(request):
    return direct_to_template(request, 'list_timeline.html',
        {'report':Report.objects.all(),},
    )

def timeline_en(request, slug):
    report = Report.objects.filter(slug=slug)
    january = Month.objects.filter(report=report)
    payload = { 'report':report, 'january':january}
    return render(request, 'home.html', payload)

def timeline_nl(request, slug):
    report = Report.objects.filter(slug=slug)
    january = Month.objects.filter(report=report)
    payload = { 'report':report, 'january':january}
    return render(request, 'home.html', payload)