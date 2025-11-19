from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('auth/', include('authentication.urls')), # Tambahkan ini
    path('admin/', admin.site.urls),
]