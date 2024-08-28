from datetime import datetime
from django import template

import locale

locale.setlocale(
   category=locale.LC_ALL,
   locale='russian'
)

register = template.Library()

@register.simple_tag()
def current_time(format_string='%d %B %Y %H:%M:%S.%f %A'): # format_string='%b %d %Y' - значение по умолчанию
   return datetime.utcnow().strftime(format_string)

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()