from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),  # Добавили эту строчку
    path("products/", include("simpleapp.urls")),
    path("accounts/", include("allauth.urls")),  # Оставили только allauth
]