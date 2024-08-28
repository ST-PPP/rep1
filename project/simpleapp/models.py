from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator

class Staff(models.Model):

    director = 'DI'
    admin = 'AD'
    cook = 'CO'
    cashier = 'CA'
    cleaner = 'CL'

    POSITIONS = [
        (director, 'Директор'),
        (admin, 'Администратор'),
        (cook, 'Повар'),
        (cashier, 'Кассир'),
        (cleaner, 'Уборщик') ]

    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices=POSITIONS, default=cashier)
    labor_contract = models.IntegerField()

    def get_last_name(self):
        return self.full_name.split()[0]

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True) # unique=True - названия товаров не должны повторяться
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products') # category - поле категории будет ссылаться на модель категории. related_name='products' - все продукты в категории будут доступны через поле products
    price = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    composition = models.TextField(default="Состав не указан")
    description = models.TextField(default="Описание не указано")

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

class Category(models.Model): # Категория, к которой будет привязываться товар
    name = models.CharField(max_length=100, unique=True) # названия категорий тоже не должны повторяться

    def __str__(self):
        return self.name.title()

class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:  # если завершён, возвращаем разность объектов
            return (self.time_out - self.time_in).total_seconds() / 60.0
        else:  # если ещё нет, то сколько длится выполнение
            return (datetime.now() - self.time_in).total_seconds() / 60.0

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    _amount = models.IntegerField(default=1, db_column = 'amount')


    def product_sum(self):
        product_price = self.product.price
        return product_price * self._amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()