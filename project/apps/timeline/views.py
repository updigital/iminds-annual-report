# coding: utf-8
from django.views.generic.simple import direct_to_template
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import *


def list_en(request):
    en = Report.objects.filter(language='EN')
    report = Report.objects.filter(language='EN')
    
    payload = {'en':en, 'report':report}
    
    return render(request, 'list.html', payload)

def list_nl(request):
    nl = Report.objects.filter(language='NL')
    report = Report.objects.filter(language='NL')
    
    payload = {'nl':nl, 'report':report}
    
    return render(request, 'list.html', payload)

def report_en(request, slug):
    en = Report.objects.filter(language='EN')
    report = Report.objects.filter(language='EN').filter(slug=slug)

    january = Month.objects.filter(language='EN').filter(report=report).filter(month='01')
    february = Month.objects.filter(language='EN').filter(report=report).filter(month='02')
    march = Month.objects.filter(language='EN').filter(report=report).filter(month='03')
    april = Month.objects.filter(language='EN').filter(report=report).filter(month='04')
    may = Month.objects.filter(language='EN').filter(report=report).filter(month='05')
    june = Month.objects.filter(language='EN').filter(report=report).filter(month='06')
    july = Month.objects.filter(language='EN').filter(report=report).filter(month='07')
    august = Month.objects.filter(language='EN').filter(report=report).filter(month='08')
    september = Month.objects.filter(language='EN').filter(report=report).filter(month='09')
    october = Month.objects.filter(language='EN').filter(report=report).filter(month='10')
    november = Month.objects.filter(language='EN').filter(report=report).filter(month='11')
    december = Month.objects.filter(language='EN').filter(report=report).filter(month='12')
    
    payload = {'en':en, 'report':report, 'january':january, 'february':february, 'march':march,
                'april':april, 'may':may, 'june':june, 'july':july, 'august':august,
                'september':september, 'october':october, 'november':november,'december':december}
    
    return render(request, 'home.html', payload)

def report_nl(request, slug):
    nl = Report.objects.filter(language='NL')
    report = Report.objects.filter(language='NL').filter(slug=slug)

    january = Month.objects.filter(language='NL').filter(report=report).filter(month='01')
    february = Month.objects.filter(language='NL').filter(report=report).filter(month='02')
    march = Month.objects.filter(language='NL').filter(report=report).filter(month='03')
    april = Month.objects.filter(language='NL').filter(report=report).filter(month='04')
    may = Month.objects.filter(language='NL').filter(report=report).filter(month='05')
    june = Month.objects.filter(language='NL').filter(report=report).filter(month='06')
    july = Month.objects.filter(language='NL').filter(report=report).filter(month='07')
    august = Month.objects.filter(language='NL').filter(report=report).filter(month='08')
    september = Month.objects.filter(language='NL').filter(report=report).filter(month='09')
    october = Month.objects.filter(language='NL').filter(report=report).filter(month='10')
    november = Month.objects.filter(language='NL').filter(report=report).filter(month='11')
    december = Month.objects.filter(language='NL').filter(report=report).filter(month='12')
    
    payload = {'nl':nl, 'report':report, 'january':january, 'february':february, 'march':march,
                'april':april, 'may':may, 'june':june, 'july':july, 'august':august,
                'september':september, 'october':october, 'november':november,'december':december}
    
    return render(request, 'home.html', payload)