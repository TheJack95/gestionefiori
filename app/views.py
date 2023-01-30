from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from app.models import Item
from app.forms import ItemForm


def index(request):
    items = Item.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        'items': items
    }
    return HttpResponse(template.render(context, request))


def add(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item_form.save()

            return HttpResponseRedirect(reverse('index'))

    return request


def delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()

    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    item_to_edit = Item.objects.get(id=id)
    items = Item.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        'items': items,
        'item_to_edit': item_to_edit
    }
    return HttpResponse(template.render(context, request))


def update_item(request, id):
    item_form = ItemForm(request.POST)
    if item_form.is_valid():
        item_to_update = Item.objects.get(id=id)
        item_to_update.ean_code = request.POST['ean_code']
        item_to_update.original_price = request.POST['original_price']
        item_to_update.price = request.POST['price']
        item_to_update.description = request.POST['description']
        item_to_update.save()

    return HttpResponseRedirect(reverse('index'))
