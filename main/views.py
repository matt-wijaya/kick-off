from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Kick Off',
        'name' : 'Matthew Wijaya',
        'class' : 'PBP '
    }

    return render(request, "main.html", context)