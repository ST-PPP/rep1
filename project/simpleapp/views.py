from django.views.generic import ListView, DetailView # Импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product
from datetime import datetime
from pprint import pprint


class ProductsList(ListView): # СТ Вывод списка товаров.
    model = Product # Указываем модель, объекты которой мы будем выводить
    ordering = 'name' # Поле, которое будет использоваться для сортировки объектов
    template_name = 'products.html' # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'products' # Это имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.

    def get_context_data(self, **kwargs): # Метод get_context_data позволяет нам изменить набор данных, который будет передан в шаблон.
        context = super().get_context_data(**kwargs) # С помощью super() мы обращаемся к родительским классам и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам. В ответе мы должны получить словарь.
        context['next_sale'] = None # Добавим ещё одну пустую переменную, чтобы на её примере рассмотреть работу ещё одного фильтра.
        return context

class ProductDetail(DetailView): # СТ Вывод одного товара.
    model = Product # Модель всё та же, но мы хотим получать информацию по отдельному товару
    template_name = 'product.html' # Используем другой шаблон — product.html
    context_object_name = 'product' # Название объекта, в котором будет выбранный пользователем продукт