# example/views.py
from datetime import datetime
from django.template import loader
from django.http import HttpResponse
import requests

def index(request):
    now = datetime.now()
    title = 'Rod Lessa - Arquiteto de Soluções'
    template = loader.get_template('index.html')
    context = {
        'now': now,
        'title': title,
    }
    return HttpResponse(template.render(context, request))

def cv(request):
    title = 'Rod Lessa - Arquiteto de Soluções'
    template = loader.get_template('cv.html')
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))

def apiexample(request):
    
    resp = requests.get("https://nekos.best/api/v2/neko")
    data = resp.json()
    loadimgneko = data["results"][0]["url"]
    print(data["results"][0]["url"])
    title = 'Rod Lessa - Arquiteto de Soluções'
    template = loader.get_template('examples.html')
    context = {
        'title': title,
        'nekoimg':loadimgneko,
    }
    return HttpResponse(template.render(context, request))
def artigos(request):
    title = 'Rod Lessa - Artigos'
    template = loader.get_template('examples.html')
    context = {
        'title': title,
        'nekoimg':loadimgneko,
    }
    return HttpResponse(template.render(context, request))