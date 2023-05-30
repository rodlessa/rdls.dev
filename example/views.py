# example/views.py
from datetime import datetime
from django.template import loader
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    template = loader.get_template('index.html')
    context = {
        'now': now,
    }
    return HttpResponse(template.render(context, request))