from django_filters import FilterSet
from .models import Product

class ProductFilter(FilterSet): # Создаем свой набор фильтров для модели Product.  FilterSet, который мы наследуем,  должен чем-то напомнить знакомые вам Django дженерики.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Подчёркнутые на скрине имена с английского на русский."D:\ST\r5h7\s4hs6\o+\СкилФэктори\стар_2\о\p+\I\$\Скрины магазина\Разн\2024-0827-1246_10-Screen Marker and Recorder.png"
#    def __init__(self, *args, **kwargs):
#        super(ProductFilter, self).__init__(*args, **kwargs)
#        self.filters['name'].label = 'Имя'
#        self.filters['quantity'].label = 'Количество'
#        self.filters['price'].label = 'Цена'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   class Meta: # В Meta классе мы должны указать Django модель,  в которой будем фильтровать записи.
       model = Product # В fields мы описываем по каким полям модели  будет производиться фильтрация.
       fields = {
           'name': ['icontains'], # поиск по названию
           # 'description': ['icontains'],  # поиск по названию
           # 'category': ['icontains'],
           'price': [
               'lt',  # цена должна быть меньше или равна указанной
               'gt',  # цена должна быть больше или равна указанной
           ],
           'quantity': ['gt'],  # количество товаров должно быть больше или равно
       }