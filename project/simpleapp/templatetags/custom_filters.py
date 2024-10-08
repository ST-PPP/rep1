from django import template

register = template.Library()

CURRENCIES_SYMBOLS = {
   'rub': '₽',
   'usd': '$',
}

@register.filter() # Регистрируем наш фильтр, чтоб Django понимал, что это именно фильтр для шаблонов, а не простая функция.
def currency(value, code='rub'): # value: значение, к которому нужно применить фильтр. code: код валюты
   postfix = CURRENCIES_SYMBOLS[code]
   return f'{value} {postfix}' # Возвращаемое функцией значение подставится в шаблон.