# example/views.py
from datetime import datetime
from django.template import loader
from django.http import HttpResponse

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
def artigos(request):
    title = 'Rod Lessa - Artigos'
    template = loader.get_template('artigos.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))