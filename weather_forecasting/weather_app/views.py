from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def abc(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())