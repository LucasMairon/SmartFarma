from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.product'
    verbose_name = 'product'

    def ready(self):
        import django.db.models.signals  # noqa (F401)
