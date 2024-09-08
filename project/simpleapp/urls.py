from django.urls import path
from .views import ProductsList, ProductDetail, ProductCreate # Импортируем созданное нами представление

urlpatterns = [
   path('', ProductsList.as_view()),  # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, чуть позже станет ясно почему. Т.к. наше объявленное представление является классом, а Django ожидает функцию, нам надо представить этот класс в виде view. Для этого вызываем метод as_view.
   path('<int:pk>', ProductDetail.as_view(), name='product_detail'), # pk — это первичный ключ товара, который будет выводиться у нас в шаблон int — указывает на то, что принимаются только целочисленные значения
   path('create/', ProductCreate.as_view(), name='product_create'),
]
