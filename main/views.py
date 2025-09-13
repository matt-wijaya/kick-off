from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Item
from main.forms import ItemForm

def show_main(request):
    items_list = Item.objects.all()

    context = {
        'app_name': 'Kick Off',
        'name' : 'Matthew Wijaya',
        'class' : 'PBP C',
        'items' : items_list
    }

    return render(request, "main.html", context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_item.html", context)

def show_items(request, id):
    item = get_object_or_404(Item, pk=id)

    context = {
        'item': item
    }

    return render(request, "item_detail.html", context)

def show_xml(request):
    items_list = Item.objects.all()
    xml_data = serializers.serialize("xml", items_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    items_list = Item.objects.all()
    json_data = serializers.serialize("json", items_list)
    return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, id):
    item = get_object_or_404(Item, pk=id)
    xml_data = serializers.serialize("xml", [item])
    return HttpResponse(xml_data, content_type="application/xml")
    
def show_json_by_id(request, id):
    item = get_object_or_404(Item, pk=id)
    json_data = serializers.serialize("json", [item])
    return HttpResponse(json_data, content_type="application/json")


