from django.views.generic import ListView # Импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product

class ProductsList(ListView):
    model = Product # Указываем модель, объекты которой мы будем выводить
    ordering = 'name' # Поле, которое будет использоваться для сортировки объектов
    template_name = 'products.html' # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'products' # Это имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.