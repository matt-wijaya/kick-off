from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return JsonResponse({
                    "status": True,
                    "message": "Login successful!",
                    "username": username
                }, status=200)
            else:
                return JsonResponse({"status": False, "message": "Account disabled."}, status=401)
        else:
            return JsonResponse({"status": False, "message": "Invalid login details."}, status=401)
    return JsonResponse({"status": False, "message": "Method not allowed"}, status=405)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            password_confirm = data.get('password_confirm')

            if password != password_confirm:
                return JsonResponse({"status": False, "message": "Passwords do not match."}, status=400)
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({"status": False, "message": "Username taken."}, status=400)
            
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({"status": True, "message": "User created!"}, status=200)
        except:
            return JsonResponse({"status": False, "message": "Invalid data"}, status=400)
    return JsonResponse({"status": False, "message": "Method not allowed"}, status=405)

@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({"status": True, "message": "Logged out successfully!", "username": username}, status=200)
    except:
        return JsonResponse({"status": False, "message": "Logout failed."}, status=401)