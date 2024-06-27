from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model): # Товар для нашей витрины
    name = models.CharField(max_length=50, unique=True) # unique=True значит названия товаров не должны повторяться
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products') # to='Category' поле категории будет ссылаться на модель категории # related_name='products' все продукты в категории будут доступны через поле products
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'



class Category(models.Model): # Категория, к которой будет привязываться товар
    name = models.CharField(max_length=100, unique=True) # названия категорий тоже не должны повторяться

    def __str__(self):
        return self.name.title()