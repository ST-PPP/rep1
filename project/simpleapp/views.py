from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView) # Импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product
from datetime import datetime
from pprint import pprint
from django.http import HttpResponse
from .filters import ProductFilter
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

class ProductsList(ListView): # СТ Вывод списка товаров.
    model = Product # Указываем модель, объекты которой мы будем выводить
    ordering = 'name' # Поле, которое будет использоваться для сортировки объектов
    template_name = 'products.html' # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'products' # Это имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 2  # вот так мы можем указать количество записей на странице

    def get_queryset(self): # Переопределяем функцию получения списка товаров
        queryset = super().get_queryset() # Получаем обычный запрос
        self.filterset = ProductFilter(self.request.GET, queryset) # Используем наш класс фильтрации. self.request.GET содержит объект QueryDict, который мы рассматривали Сохраняем нашу фильтрацию в объекте класса, чтобы потом добавить в контекст и использовать в шаблоне.
        return self.filterset.qs # Возвращаем из функции отфильтрованный список товаров

    def get_context_data(self, **kwargs): # Метод get_context_data позволяет нам изменить набор данных, который будет передан в шаблон.
        context = super().get_context_data(**kwargs) # С помощью super() мы обращаемся к родительским классам и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам. В ответе мы должны получить словарь.
        context['next_sale'] = None # Добавим ещё одну пустую переменную, чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['filterset'] = self.filterset # Добавляем в контекст объект фильтрации.
        return context

class ProductDetail(DetailView): # СТ Вывод одного товара.
    model = Product # Модель всё та же, но мы хотим получать информацию по отдельному товару
    template_name = 'product.html' # Используем другой шаблон — product.html
    context_object_name = 'product' # Название объекта, в котором будет выбранный пользователем продукт

def multiply(request): # калькулятор в URL.
   number = request.GET.get('number')
   multiplier = request.GET.get('multiplier')

   try:
       result = int(number) * int(multiplier)
       html = f"<html><body>{number}*{multiplier}={result}</body></html>"
   except (ValueError, TypeError):
       html = f"<html><body>Invalid input.</body></html>"

   return HttpResponse(html)


class ProductCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView): # Добавляем новое представление для создания товаров. PermissionRequiredMixin - добавили проверку прав при входе.
    permission_required = ('simpleapp.add_product',) # строка относится к проверке прав при входе
    raise_exception = True
    form_class = ProductForm # Указываем нашу разработанную форму
    model = Product # модель товаров
    template_name = 'product_edit.html' # и новый шаблон, в котором используется форма.


class ProductUpdate(PermissionRequiredMixin, UpdateView): # Добавляем представление для изменения товара.
    permission_required = ('simpleapp.change_product',)
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductDelete(PermissionRequiredMixin, DeleteView): # Представление удаляющее товар.
    permission_required = ('simpleapp.delete_product',)
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list') # product_list - путь куда перенаправится пользователь после удаления товара.