from django.apps import AppConfig


class OrderItemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.order_item'
    verbose_name = 'order_item'

    def ready(self):
        import django.db.models.signals
