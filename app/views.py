from django.http import HttpResponse
from django.template import loader

from app.models import Item
from app.forms import ItemForm


def index(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

    items = Item.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        'items': items
    }
    return HttpResponse(template.render(context, request))
