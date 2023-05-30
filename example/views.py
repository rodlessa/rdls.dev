import datetime
from django.template import loader
from django.http import HttpResponse


def index(request):
    now = datetime.datetime.now()
    template = loader.get_template('index.html')
    title = 'Rod Lessa - Analista de Infraestrutura | Dev Ops'
    context = {
        'now':now,
        'title':title,
    }
    return HttpResponse(template.render(context,request))