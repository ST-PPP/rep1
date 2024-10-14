"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from simpleapp.views import multiply

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('products/', include('simpleapp.urls')), # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) подключались к главному приложению с префиксом products/.
    path('multiply/', multiply),
    path("accounts/", include('allauth.urls')), # то что слева, это взамен на то что справа от данных слов. path('accounts/', include('django.contrib.auth.urls')), path('accounts/', include('accounts.urls')), СТ чтобы страница регистрации и авторизации была с возможностью авторизироваться через яндекс аккаунт


]
