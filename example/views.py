# example/views.py
from datetime import datetime
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def namepage(request):
    name = {'title': 'RodLessa - Consultoria em TI'}
    context = {
        'name': name        }
    template = loader.get_template('index.html')
    return render(request, 'index.html', context)