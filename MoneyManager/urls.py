from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('mainapp.urls', namespace="main")),
    path('auth/', include('authapp.urls', namespace="auth")),
    path('admin/', admin.site.urls),
]
