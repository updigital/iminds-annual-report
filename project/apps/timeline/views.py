# coding: utf-8
from django.views.generic.simple import direct_to_template
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import *


#January
def milestone_january_en(request):
    return direct_to_template(request, 'milestones/en/january.html',
)
def milestone_january_nl(request):
    return direct_to_template(request, 'milestones/nl/january.html',
)

#February
def milestone_february_en(request):
    return direct_to_template(request, 'milestones/en/february.html',
)
def milestone_february_nl(request):
    return direct_to_template(request, 'milestones/nl/february.html',
)

def highlight_february_en(request):
    return direct_to_template(request, 'highlights/en/february.html',
)
def highlight_february_nl(request):
    return direct_to_template(request, 'highlights/nl/february.html',
)

#March
def milestone_march_en(request):
    return direct_to_template(request, 'milestones/en/march.html',
)
def milestone_march_nl(request):
    return direct_to_template(request, 'milestones/nl/march.html',
)

def highlight_march_en(request):
    return direct_to_template(request, 'highlights/en/march.html',
)
def highlight_march_nl(request):
    return direct_to_template(request, 'highlights/nl/march.html',
)

#April
def milestone_april_en(request):
    return direct_to_template(request, 'milestones/en/april.html',
)
def milestone_april_nl(request):
    return direct_to_template(request, 'milestones/nl/april.html',
)

def highlight_april_en(request):
    return direct_to_template(request, 'highlights/en/april.html',
)
def highlight_april_nl(request):
    return direct_to_template(request, 'highlights/nl/april.html',
)

def highlight_april_02_en(request):
    return direct_to_template(request, 'highlights/en/april-02.html',
)
def highlight_april_02_nl(request):
    return direct_to_template(request, 'highlights/nl/april-02.html',
)

#May
def milestone_may_en(request):
    return direct_to_template(request, 'milestones/en/may.html',
)
def milestone_may_nl(request):
    return direct_to_template(request, 'milestones/nl/may.html',
)

def highlight_may_en(request):
    return direct_to_template(request, 'highlights/en/may.html',
)
def highlight_may_nl(request):
    return direct_to_template(request, 'highlights/nl/may.html',
)

#June
def highlight_june_en(request):
    return direct_to_template(request, 'highlights/en/june.html',
)
def highlight_june_nl(request):
    return direct_to_template(request, 'highlights/nl/june.html',
)

def highlight_june_02_en(request):
    return direct_to_template(request, 'highlights/en/june-02.html',
)
def highlight_june_02_nl(request):
    return direct_to_template(request, 'highlights/nl/june-02.html',
)

#July
def highlight_july_en(request):
    return direct_to_template(request, 'highlights/en/july.html',
)
def highlight_july_nl(request):
    return direct_to_template(request, 'highlights/nl/july.html',
)

#August
def highlight_august_en(request):
    return direct_to_template(request, 'highlights/en/august.html',
)
def highlight_august_nl(request):
    return direct_to_template(request, 'highlights/nl/august.html',
)

#September
def milestone_september_en(request):
    return direct_to_template(request, 'milestones/en/september.html',
)
def milestone_september_nl(request):
    return direct_to_template(request, 'milestones/nl/september.html',
)

def highlight_september_en(request):
    return direct_to_template(request, 'highlights/en/september.html',
)
def highlight_september_nl(request):
    return direct_to_template(request, 'highlights/nl/september.html',
)

#October
def milestone_october_en(request):
    return direct_to_template(request, 'milestones/en/october.html',
)
def milestone_october_nl(request):
    return direct_to_template(request, 'milestones/nl/october.html',
)

def milestone_october_02_en(request):
    return direct_to_template(request, 'milestones/en/october-02.html',
)
def milestone_october_02_nl(request):
    return direct_to_template(request, 'milestones/nl/october-02.html',
)

def highlight_october_en(request):
    return direct_to_template(request, 'highlights/en/october.html',
)
def highlight_october_nl(request):
    return direct_to_template(request, 'highlights/nl/october.html',
)
    
def highlight_october_02_en(request):
    return direct_to_template(request, 'highlights/en/october-02.html',
)
def highlight_october_02_nl(request):
    return direct_to_template(request, 'highlights/nl/october-02.html',
)

#November
def milestone_november_en(request):
    return direct_to_template(request, 'milestones/en/november.html',
)
def milestone_november_nl(request):
    return direct_to_template(request, 'milestones/nl/november.html',
)

#December
def milestone_december_en(request):
    return direct_to_template(request, 'milestones/en/december.html',
)
def milestone_december_nl(request):
    return direct_to_template(request, 'milestones/nl/december.html',
)

def highlight_december_en(request):
    return direct_to_template(request, 'highlights/en/december.html',
)
def highlight_december_nl(request):
    return direct_to_template(request, 'highlights/nl/december.html',
)

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
    
    return render(request, 'home_nl.html', payload)