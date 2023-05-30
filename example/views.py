import datetime
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    title = 'Rod Lessa - Analista de Infraestrutura | Dev Ops'
    context = {
        'title':title,
    }
    return HttpResponse(template.render(context,request))