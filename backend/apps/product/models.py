from django.db import models
from apps.shared.utils import resize_image
from .validators import (
    name_regex_validator,
    brand_regex_validator,
    maker_regex_validator,
    qrcode_regex_validator,
    sku_regex_validator,
)


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Nome',
        validators=[name_regex_validator]
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Preco')
    available_quantity = models.IntegerField(
        verbose_name='Quantidade disponível')
    description = models.TextField(max_length=150, verbose_name='Descrição')
    brand = models.CharField(
        max_length=20,
        verbose_name='Marca',
        validators=[brand_regex_validator]
    )
    maker = models.CharField(
        max_length=30,
        verbose_name='Fabricante',
        validators=[maker_regex_validator]
    )
    weight = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Peso')
    ean = models.CharField(
        max_length=13,
        verbose_name='Código de barras',
        validators=[qrcode_regex_validator]
    )
    sku = models.CharField(
        max_length=13,
        verbose_name='SKU',
        validators=[sku_regex_validator]
    )
    image = models.ImageField(
        upload_to='Imagem_Produto/%Y/%m'
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        nova_largura = 600

        if self.image:
            resize_image(self.image, nova_largura)
