from django.http import HttpResponseRedirect, HttpResponse, JsonResponse 
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt 
from django.utils.html import strip_tags 
import datetime
import json 

from main.models import Item
from main.forms import ItemForm

@login_required(login_url='/login')
def show_main(request):
    # Hapus logika items_list yang lama
    context = {
        'app_name': 'Kick Off',
        'name' : request.user.username,
        'class' : 'PBP C',
        'form' : ItemForm(), 
        'last_login' : request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

def get_items_json(request):
    filter_type = request.GET.get("filter", "all")
    
    if filter_type == "all":
        items_list = Item.objects.all()
    else:
        if not request.user.is_authenticated:
             return JsonResponse({'status': 'error', 'message': 'You must be logged in to view your items.'}, status=401)
        items_list = Item.objects.filter(store=request.user)
    
    return HttpResponse(serializers.serialize("json", items_list), content_type="application/json")

@csrf_exempt 
@login_required(login_url='/login')
def create_item_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data."}, status=400)
        
        # Lakukan Sanitasi Manual untuk Data JSON POST (Defense-in-Depth)
        if 'name' in data:
            data['name'] = strip_tags(data['name'])
        if 'description' in data:
            data['description'] = strip_tags(data['description'])
            
        form = ItemForm(data)
        
        if form.is_valid():
            item_entry = form.save(commit = False)
            item_entry.store = request.user
            item_entry.save()
            return JsonResponse({"status": "success", "message": "Item successfully added!", "item_id": item_entry.pk}, status=201)
        else:
            return JsonResponse({"status": "error", "message": "Failed to add item.", "errors": form.errors}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

@csrf_exempt
@login_required(login_url='/login')
def update_item_ajax(request, id):
    item = get_object_or_404(Item, pk=id)
    
    if item.store != request.user:
        return JsonResponse({"status": "error", "message": "You are not authorized to edit this item."}, status=403)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data."}, status=400)

        # Lakukan Sanitasi Manual untuk Data JSON POST (Defense-in-Depth)
        if 'name' in data:
            data['name'] = strip_tags(data['name'])
        if 'description' in data:
            data['description'] = strip_tags(data['description'])
            
        form = ItemForm(data, instance=item)
        
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": f"Item '{item.name}' successfully updated!"}, status=200)
        else:
            return JsonResponse({"status": "error", "message": "Failed to update item.", "errors": form.errors}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

@csrf_exempt
@login_required(login_url='/login')
def delete_item_ajax(request, id):
    item = get_object_or_404(Item, pk=id)
    
    if item.store != request.user:
        return JsonResponse({"status": "error", "message": "You are not authorized to delete this item."}, status=403)

    if request.method == 'POST':
        item_name = item.name 
        item.delete()
        return JsonResponse({"status": "success", "message": f"Item '{item_name}' successfully deleted!"}, status=200)

    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

def register(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            message = 'Your account has been successfully created! Please log in.'
            
            if is_ajax:
                return JsonResponse({"status": "success", "message": message}, status=201)
            else:
                messages.success(request, message)
                return redirect('main:login')
        else:
            if is_ajax:
                return JsonResponse({"status": "error", "message": "Registration failed.", "errors": form.errors}, status=400)
            else:
                pass 
    
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            response_data = {"status": "success", "message": f"Welcome back, {user.username}!"}
            
            if is_ajax:
                response = JsonResponse(response_data)
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))

            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            if is_ajax:
                return JsonResponse({"status": "error", "message": "Invalid username or password. Please try again."}, status=400)
            else:
                pass 
    
    form = AuthenticationForm() 
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    username = request.user.username 
    logout(request)
    
    message = f"Goodbye, {username}. You have been logged out."

    if is_ajax:
        response = JsonResponse({"status": "success", "message": message})
        response.delete_cookie('last_login')
        return response
    
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    messages.success(request, message)
    return response

def item_detail(request, id):
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


