from django.apps import AppConfig


class SimpleappConfig(AppConfig):
    verbose_name = 'Публикации'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpleapp'
