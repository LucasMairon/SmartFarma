# Generated by Django 5.1.1 on 2024-10-15 00:29

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='O nome deve conter apenas letras', regex='^[a-zá-ùA-ZÁ-Ù0-9]+(?:[\\s][a-zá-ùA-ZÁ-Ù0-9]+)+$')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='complement',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='O nome deve conter apenas letras', regex='^[a-zá-ùA-ZÁ-Ù0-9]+(?:[\\s][a-zá-ùA-ZÁ-Ù0-9]+)+$')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='neighborhood',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='O nome deve conter apenas letras', regex='^[a-zá-ùA-ZÁ-Ù0-9]+(?:[\\s][a-zá-ùA-ZÁ-Ù0-9]+)+$')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='O nome deve conter apenas letras', regex='^[a-zá-ùA-ZÁ-Ù0-9-]+(?:[\\s][a-zá-ùA-ZÁ-Ù0-9-]+)+$')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='reference_point',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='O nome deve conter apenas letras', regex='^[a-zá-ùA-ZÁ-Ù0-9]+(?:[\\s][a-zá-ùA-ZÁ-Ù0-9]+)+$')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='O nome deve conter apenas letras', regex='^[a-zá-ùA-ZÁ-Ù0-9]+(?:[\\s][a-zá-ùA-ZÁ-Ù0-9]+)+$')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='O nome deve conter apenas letras', regex='^[a-zá-ùA-ZÁ-Ù0-9]+(?:[\\s][a-zá-ùA-ZÁ-Ù0-9]+)+$')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='O CEP deve conter 8 números', regex='^[0-9]{8}$')]),
        ),
    ]
